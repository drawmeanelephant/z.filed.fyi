#!/usr/bin/env python3
"""Re-check the facts this site asserts against their live sources.

Content drift is invisible in a static site: a star count or a changelog
version written into a page stays wrong until a human notices. This script
compares the claims recorded in `scripts/claims.json` against the live sources
and reports anything that has moved.

Design notes:

- Tolerances exist because most of these values move constantly. A star count
  checked weekly will differ from the recorded figure every time; raising an
  issue for that would be noise. `star_tolerance_k` absorbs routine drift, and
  a real problem (a repo renamed, deleted, relicensed, or jumping a major
  version) still trips it.
- Exit code is 0 when everything is in range and 1 on any drift or fetch
  failure, so the workflow can branch on it.
- `--json` emits a machine-readable report the workflow turns into an issue.
- Network failures are reported as `error`, never silently treated as "fine".
  A checker that cannot reach the internet must not report success.

Usage:
    python3 scripts/check-freshness.py [--json] [--only github|repos|changelogs|model_releases]
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
CLAIMS = ROOT / "scripts" / "claims.json"
TIMEOUT = 30
UA = "z-filed-freshness-check/1.0 (+https://z.filed.fyi)"

# One cached fetch per URL: several checks can need the same changelog page.
_CACHE: dict[str, str] = {}


def fetch(url: str) -> str:
    """GET a URL as text, raising on any failure. Results are cached."""
    if url in _CACHE:
        return _CACHE[url]
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        text = resp.read().decode("utf-8", errors="replace")
    _CACHE[url] = text
    return text


def fetch_json(url: str, token: str | None = None):
    headers = {"User-Agent": UA, "Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def semver_key(v: str) -> tuple:
    """Sort key for a dotted version, tolerant of a leading 'v' and suffixes."""
    core = v.lstrip("vV").split("-")[0]
    parts = []
    for p in core.split("."):
        digits = re.sub(r"\D", "", p)
        parts.append(int(digits) if digits else 0)
    while len(parts) < 3:
        parts.append(0)
    return tuple(parts[:3])


# ---------------------------------------------------------------- checks


def check_github(claims: dict, token: str | None) -> list[dict]:
    out = []
    for org, repos in claims.items():
        if org.startswith("_"):
            continue
        for repo, spec in repos.items():
            if repo.startswith("_"):
                continue
            name = f"{org}/{repo}"
            expected = spec["value"]
            tol = int(spec.get("star_tolerance_k", 0.5) * 1000)
            try:
                data = fetch_json(f"https://api.github.com/repos/{name}", token)
            except urllib.error.HTTPError as e:
                out.append(
                    {
                        "check": "github",
                        "id": name,
                        "status": "error",
                        "detail": f"HTTP {e.code} fetching repo metadata",
                        "page": spec.get("page"),
                    }
                )
                continue
            except Exception as e:  # noqa: BLE001 - report, never mask
                out.append(
                    {
                        "check": "github",
                        "id": name,
                        "status": "error",
                        "detail": f"{type(e).__name__}: {e}",
                        "page": spec.get("page"),
                    }
                )
                continue

            live = data.get("stargazers_count")
            if live is None:
                out.append(
                    {
                        "check": "github",
                        "id": name,
                        "status": "error",
                        "detail": "no stargazers_count in response",
                        "page": spec.get("page"),
                    }
                )
            elif abs(live - expected) <= tol:
                out.append(
                    {
                        "check": "github",
                        "id": name,
                        "status": "ok",
                        "expected": expected,
                        "live": live,
                        "page": spec.get("page"),
                    }
                )
            else:
                out.append(
                    {
                        "check": "github",
                        "id": name,
                        "status": "drift",
                        "expected": expected,
                        "live": live,
                        "delta": live - expected,
                        "tolerance": tol,
                        "detail": "star count moved beyond tolerance",
                        "page": spec.get("page"),
                    }
                )
    return out


def check_repos(claims: dict, token: str | None) -> list[dict]:
    out = []
    for name, spec in claims.items():
        if name.startswith("_"):
            continue
        try:
            data = fetch_json(f"https://api.github.com/repos/{name}", token)
        except Exception as e:  # noqa: BLE001
            out.append(
                {
                    "check": "repos",
                    "id": name,
                    "status": "error",
                    "detail": f"{type(e).__name__}: {e}",
                }
            )
            continue
        live_lic = (data.get("license") or {}).get("spdx_id")
        live_created = (data.get("created_at") or "")[:10]
        problems = []
        if live_lic != spec["license"]:
            problems.append(f"license is {live_lic!r}, site says {spec['license']!r}")
        if live_created != spec["created"]:
            problems.append(
                f"created {live_created}, site says {spec['created']}"
            )
        out.append(
            {
                "check": "repos",
                "id": name,
                "status": "drift" if problems else "ok",
                "live_license": live_lic,
                "live_created": live_created,
                "detail": "; ".join(problems) or None,
            }
        )
    return out


def parse_zcode_changelog(html: str) -> list[tuple[str, str]]:
    pairs = re.findall(
        r">(v?\d+\.\d+\.\d+)</span><span[^>]*>Released ([A-Z][a-z]{2} \d{1,2}, \d{4})</span>",
        html,
    )
    out = []
    for v, d in pairs:
        dt = f"{d.split()[1]} {d.split()[0]} {d.split()[2]}"  # "29 Sep 2026"
        out.append((v.lstrip("v"), dt))
    return out


def parse_autoclaw_changelog(html: str) -> list[tuple[str, str]]:
    out = []
    for m in re.finditer(r'changelog-version">v?(\d+\.\d+\.\d+)<', html):
        seg = html[m.start() : m.start() + 600]
        d = re.search(r"(\d{4}-\d{2}-\d{2})", seg)
        out.append((m.group(1), d.group(1) if d else ""))
    return out


def check_changelogs(claims: dict) -> list[dict]:
    out = []
    for key, spec in claims.items():
        if key.startswith("_"):
            continue
        url = spec["url"]
        try:
            html = fetch(url)
        except Exception as e:  # noqa: BLE001
            out.append(
                {
                    "check": "changelogs",
                    "id": key,
                    "status": "error",
                    "detail": f"{type(e).__name__}: {e}",
                    "page": spec.get("page"),
                }
            )
            continue

        if key == "zcode":
            releases = parse_zcode_changelog(html)
        elif key == "autoclaw":
            releases = parse_autoclaw_changelog(html)
        else:
            out.append(
                {
                    "check": "changelogs",
                    "id": key,
                    "status": "error",
                    "detail": f"no parser for {key}",
                }
            )
            continue

        if not releases:
            # Structure changed: the site may be fine, but we can no longer tell.
            out.append(
                {
                    "check": "changelogs",
                    "id": key,
                    "status": "error",
                    "detail": "no versions parsed; the page markup likely changed",
                    "page": spec.get("page"),
                }
            )
            continue

        newest = max(releases, key=lambda r: semver_key(r[0]))
        recorded = spec["version"]
        if semver_key(newest[0]) == semver_key(recorded):
            out.append(
                {
                    "check": "changelogs",
                    "id": key,
                    "status": "ok",
                    "expected": recorded,
                    "live": newest[0],
                    "page": spec.get("page"),
                }
            )
        elif semver_key(newest[0]) > semver_key(recorded):
            out.append(
                {
                    "check": "changelogs",
                    "id": key,
                    "status": "drift",
                    "expected": recorded,
                    "live": newest[0],
                    "detail": f"newer release published {newest[1] or 'recently'}",
                    "page": spec.get("page"),
                }
            )
        else:
            out.append(
                {
                    "check": "changelogs",
                    "id": key,
                    "status": "drift",
                    "expected": recorded,
                    "live": newest[0],
                    "detail": "site cites a newer version than the changelog shows",
                    "page": spec.get("page"),
                }
            )
    return out


def check_model_releases(claims: dict) -> list[dict]:
    url = claims["url"]
    try:
        html = fetch(url)
    except Exception as e:  # noqa: BLE001
        return [
            {
                "check": "model_releases",
                "id": "docs.z.ai release notes",
                "status": "error",
                "detail": f"{type(e).__name__}: {e}",
            }
        ]

    # Each entry is rendered as an Update component carrying the date as its
    # label and the model as its description, e.g.
    #   _jsx(Update,{label:`2026-08-26`,description:` GLM-5.3-Flash`,id:`2026-08-26`
    # Pairing them from that component is reliable; the rendered text alone puts
    # dates in a table of contents far away from the model names.
    pairs = re.findall(
        r"label:`(20\d\d-\d\d-\d\d)`[^`]{0,80}?description:`\s*([^`]{1,60}?)`",
        html,
    )
    if not pairs:
        return [
            {
                "check": "model_releases",
                "id": "docs.z.ai release notes",
                "status": "error",
                "detail": "no release entries parsed; the page markup likely changed",
            }
        ]

    out = []
    for date, spec in claims["dates"].items():
        model = spec["model"]
        dated = [desc.strip() for d, desc in pairs if d == date]
        # A later release of the same line can share a date, so match on the
        # model name appearing in that date's descriptions.
        if any(model in desc for desc in dated):
            out.append(
                {
                    "check": "model_releases",
                    "id": f"{model} @ {date}",
                    "status": "ok",
                    "page": spec.get("page"),
                }
            )
        else:
            out.append(
                {
                    "check": "model_releases",
                    "id": f"{model} @ {date}",
                    "status": "drift",
                    "detail": (
                        f"no release-notes entry for {model} dated {date}; "
                        f"that date lists: {dated or 'nothing'}"
                    ),
                    "page": spec.get("page"),
                }
            )
    return out


# ---------------------------------------------------------------- report


def render_text(results: list[dict]) -> str:
    lines = []
    for r in results:
        mark = {"ok": "OK  ", "drift": "DRIFT", "error": "ERROR"}[r["status"]]
        extra = ""
        if r["status"] == "drift":
            if "expected" in r and "live" in r:
                extra = f"  (site: {r['expected']} -> live: {r['live']})"
            if r.get("detail"):
                extra += f"  {r['detail']}"
        elif r["status"] == "error" and r.get("detail"):
            extra = f"  {r['detail']}"
        page = f"  [{r['page']}]" if r.get("page") else ""
        lines.append(f"{mark:5} {r['check']:<15} {r['id']}{extra}{page}")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true", help="emit a JSON report")
    ap.add_argument(
        "--only",
        choices=["github", "repos", "changelogs", "model_releases"],
        help="run a single check group",
    )
    args = ap.parse_args()

    claims = json.loads(CLAIMS.read_text(encoding="utf-8"))
    token = os.environ.get("GITHUB_TOKEN") or None

    results: list[dict] = []
    if not args.only or args.only == "github":
        results += check_github(claims["github"], token)
    if not args.only or args.only == "repos":
        results += check_repos(claims["repos"], token)
    if not args.only or args.only == "changelogs":
        results += check_changelogs(claims["changelogs"])
    if not args.only or args.only == "model_releases":
        results += check_model_releases(claims["model_releases"])

    drift = [r for r in results if r["status"] == "drift"]
    errors = [r for r in results if r["status"] == "error"]
    ok = [r for r in results if r["status"] == "ok"]

    if args.json:
        print(
            json.dumps(
                {
                    "total": len(results),
                    "ok": len(ok),
                    "drift": len(drift),
                    "errors": len(errors),
                    "results": results,
                },
                indent=2,
            )
        )
    else:
        print(render_text(results))
        print(f"\n{len(ok)} ok · {len(drift)} drift · {len(errors)} error")

    return 1 if (drift or errors) else 0


if __name__ == "__main__":
    sys.exit(main())
