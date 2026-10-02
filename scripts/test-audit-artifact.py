#!/usr/bin/env python3
"""Regression tests for scripts/audit-artifact.py — stdlib only.

Proves the properties the audit must keep, independent of this checkout's
location:

  1. Path independence — the audit resolves public/, content/, and itself
     relative to its repository, not the current working directory. Verified
     both on the real artifact (run from /, the repo root, and a nested
     directory) and on a minimal fixture site (run from three different
     working directories).
  2. Fail closed — a missing required input, an empty artifact, or any failed
     check produces a nonzero exit and never a pass.
  3. Representative failures — each audit check catches the defect it exists
     for (external resource, hash mismatch, stub page, rag leftovers, …).
  4. Enforcement — the deploy pipeline's `set -euo pipefail` + audit ordering
     stops before upload when the audit fails.

Run: python3 scripts/test-audit-artifact.py
"""
import json
import hashlib
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = pathlib.Path(__file__).resolve().parent
AUDIT = SCRIPTS / "audit-artifact.py"
REPO = SCRIPTS.parent

CSS_BODY = "/* fixture theme */ body{color:#111}\n"
ZAIJS_BODY = 'var mirrored = ["/"];\n'
SEARCHJS_BODY = 'function render(){className = "search-result-link"}\n'
RAG_BODY = "<file path=\"index.md\">\n<content>\n# home\n</content>\n</file>\n"
SNIPPET = "Full body text of the fixture home page, well past the forty character floor."


def sha8(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()[:8]


def build_fixture(root):
    """A minimal site that passes every audit check; tests mutate copies."""
    (root / "scripts").mkdir(parents=True)
    (root / "content" / "zh").mkdir(parents=True)
    (root / "public" / "zh").mkdir(parents=True)
    (root / "public" / "assets" / "css").mkdir(parents=True)
    (root / "public" / "assets" / "js").mkdir(parents=True)
    (root / "public" / "graph").mkdir(parents=True)
    (root / "public" / "rag-archive").mkdir(parents=True)
    shutil.copy(AUDIT, root / "scripts" / "audit-artifact.py")

    (root / "content" / "index.md").write_text("# Home\n\nFixture body.\n", encoding="utf-8")
    (root / "content" / "zh" / "index.md").write_text("# 首页\n\nFixture body.\n", encoding="utf-8")

    css = root / "public" / "assets" / "css" / "site.css"
    css.write_text(CSS_BODY, encoding="utf-8")
    v = sha8(css)
    (root / "public" / "assets" / "js" / "zai.js").write_text(ZAIJS_BODY, encoding="utf-8")
    (root / "public" / "assets" / "js" / "search.js").write_text(SEARCHJS_BODY, encoding="utf-8")

    def page(canonical, other, switch_href, switch_lang):
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{canonical}">
<link rel="alternate" hreflang="zh-CN" href="{other}">
<link rel="alternate" hreflang="x-default" href="{canonical}">
</head><body>
<a id="lang-switch" href="{switch_href}" hreflang="{switch_lang}">切换</a>
<link rel="stylesheet" href="/assets/css/site.css?v={v}">
<script src="/assets/js/zai.js?v={sha8(root / 'public' / 'assets' / 'js' / 'zai.js')}"></script>
</body></html>
"""

    (root / "public" / "index.html").write_text(
        page("https://z.filed.fyi/", "https://z.filed.fyi/zh/", "/zh/", "zh-CN"), encoding="utf-8")
    (root / "public" / "zh" / "index.html").write_text(
        page("https://z.filed.fyi/zh/", "https://z.filed.fyi/", "/", "en"), encoding="utf-8")
    (root / "public" / "404.html").write_text(
        '<!DOCTYPE html><html lang="en"><title>Page not found</title></html>', encoding="utf-8")

    search = [
        {"u": "/", "s": SNIPPET},
        {"u": "/zh/", "s": SNIPPET},
    ]
    (root / "public" / "search.json").write_text(json.dumps(search), encoding="utf-8")
    (root / "public" / "sitemap.xml").write_text(
        "<urlset><url><loc>https://z.filed.fyi/</loc></url>"
        "<url><loc>https://z.filed.fyi/zh/</loc></url></urlset>", encoding="utf-8")
    (root / "public" / "rag-archive" / "rag-content.md").write_text(RAG_BODY, encoding="utf-8")
    (root / "public" / "graph" / "data.json").write_text(json.dumps({
        "nodes": [{"id": "index", "type": "page", "stub": False, "render": True}],
        "edges": [],
    }), encoding="utf-8")
    return root


class AuditResult:
    def __init__(self, code, out):
        self.code = code
        self.out = out


def run_audit(root, cwd):
    proc = subprocess.run(
        [sys.executable, str(root / "scripts" / "audit-artifact.py")],
        cwd=str(cwd), capture_output=True, text=True, timeout=120,
    )
    return AuditResult(proc.returncode, proc.stdout + proc.stderr)


class FixtureCase(unittest.TestCase):
    """Each test gets a fresh copy of the passing fixture site."""

    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp(prefix="audit-fixture-"))
        build_fixture(self.tmp)
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def audit_from_root(self):
        return run_audit(self.tmp, cwd=self.tmp)

    def assert_pass(self, res):
        self.assertEqual(res.code, 0, f"expected pass, got {res.code}:\n{res.out}")
        self.assertIn("ARTIFACT AUDIT: all", res.out)

    def assert_fail(self, res, needle):
        self.assertNotEqual(res.code, 0, f"expected failure, got pass:\n{res.out}")
        self.assertIn(needle, res.out, f"exit {res.code} but no {needle!r}:\n{res.out}")

    def write_page(self, rel, html):
        p = self.tmp / "public" / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(html, encoding="utf-8")


class TestPassingFixture(FixtureCase):
    def test_consistent_fixture_passes(self):
        self.assert_pass(self.audit_from_root())

    def test_fixture_passes_from_outside_and_nested_cwd(self):
        for cwd in ("/", self.tmp / "public", pathlib.Path(tempfile.gettempdir())):
            with self.subTest(cwd=str(cwd)):
                self.assert_pass(run_audit(self.tmp, cwd=cwd))


class TestPathIndependence(FixtureCase):
    def test_no_absolute_local_paths_in_script(self):
        # The regression this suite exists for: the audit once hardcoded a
        # local checkout path and silently audited the wrong tree.
        src = AUDIT.read_text(encoding="utf-8")
        self.assertNotIn("/Users/", src)
        self.assertNotIn(str(REPO), src)

    def test_real_artifact_audited_identically_from_any_cwd(self):
        from_root = run_audit(REPO, cwd=REPO)
        self.assertEqual(from_root.code, 0, f"repo artifact should pass:\n{from_root.out}")
        from_slash = run_audit(REPO, cwd="/")
        self.assertEqual(from_root.code, from_slash.code)
        self.assertEqual(from_root.out, from_slash.out)

    def test_fixture_results_cwd_invariant_even_when_failing(self):
        (self.tmp / "public" / "search.json").unlink()
        outs = [run_audit(self.tmp, cwd=c).code for c in (self.tmp, "/", self.tmp / "public" / "zh")]
        self.assertTrue(outs[0] != 0)
        self.assertEqual(len(set(outs)), 1, f"exit codes differ by cwd: {outs}")


class TestFailClosed(FixtureCase):
    def test_missing_public_dir(self):
        shutil.rmtree(self.tmp / "public")
        res = self.audit_from_root()
        self.assertEqual(res.code, 2)
        self.assertIn("missing public/", res.out)

    def test_missing_content_dir(self):
        shutil.rmtree(self.tmp / "content")
        res = self.audit_from_root()
        self.assertEqual(res.code, 2)
        self.assertIn("missing content/", res.out)

    def test_empty_artifact(self):
        shutil.rmtree(self.tmp / "public")
        (self.tmp / "public").mkdir()
        res = self.audit_from_root()
        self.assertEqual(res.code, 2)
        self.assertIn("no index.html", res.out)

    def test_public_dir_without_pages_fails_not_passes(self):
        # An artifact with stray files but no pages must not pass vacuously.
        shutil.rmtree(self.tmp / "public")
        (self.tmp / "public").mkdir()
        (self.tmp / "public" / "robots.txt").write_text("User-agent: *\n", encoding="utf-8")
        self.assertEqual(self.audit_from_root().code, 2)

    def test_required_inputs_missing(self):
        # 404.html is deliberately not here: its absence is a named check
        # (test_missing_404), not an input error.
        for rel in ("search.json", "sitemap.xml",
                    "assets/js/zai.js", "assets/js/search.js"):
            with self.subTest(input=rel):
                (self.tmp / "public" / rel).unlink()
                res = self.audit_from_root()
                self.assertEqual(res.code, 2, res.out)
                self.assertIn(rel, res.out)
                (self.tmp / "public" / rel).parent.mkdir(parents=True, exist_ok=True)
                (self.tmp / "public" / rel).write_text("x", encoding="utf-8")
                if rel == "search.json":
                    (self.tmp / "public" / rel).write_text(json.dumps(
                        [{"u": "/", "s": SNIPPET}, {"u": "/zh/", "s": SNIPPET}]), encoding="utf-8")

    def test_empty_rag_bundle(self):
        # Present but zero bytes: the deployed corpus must never be empty.
        (self.tmp / "public" / "rag-archive" / "rag-content.md").write_text("", encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "rag-archive contains only rag-content.md")

    def test_unreadable_search_json(self):
        (self.tmp / "public" / "search.json").write_text("{not json", encoding="utf-8")
        self.assertEqual(self.audit_from_root().code, 2)


class TestRepresentativeFailures(FixtureCase):
    def test_external_resource_load(self):
        p = self.tmp / "public" / "index.html"
        p.write_text(p.read_text(encoding="utf-8").replace(
            "</head>", '<script src="https://cdn.example.net/x.js"></script></head>'), encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "no external resource loads")

    def test_unversioned_asset_ref(self):
        p = self.tmp / "public" / "index.html"
        p.write_text(re.sub(r"\?v=[a-f0-9]+", "", p.read_text(encoding="utf-8")), encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "all asset URLs cache-busted")

    def test_cache_bust_hash_mismatch(self):
        (self.tmp / "public" / "assets" / "css" / "site.css").write_text(
            CSS_BODY + "p{color:#222}\n", encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "cache-bust hashes match file contents")

    def test_leftover_prune_asset(self):
        (self.tmp / "public" / "assets" / "css" / "theme.css").write_text("body{}", encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "FAIL prune")

    def test_canonical_mismatch(self):
        p = self.tmp / "public" / "index.html"
        p.write_text(p.read_text(encoding="utf-8").replace(
            'href="https://z.filed.fyi/"', 'href="https://z.filed.fyi/wrong/"'), encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "canonical URLs match page locations")

    def test_missing_hreflang(self):
        p = self.tmp / "public" / "zh" / "index.html"
        p.write_text(p.read_text(encoding="utf-8").replace('hreflang="zh-CN" href', 'rel="x" href'), encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "hreflang en/zh-CN/x-default")

    def test_missing_lang_switch(self):
        p = self.tmp / "public" / "zh" / "index.html"
        p.write_text(p.read_text(encoding="utf-8").replace('id="lang-switch"', 'id="nope"'), encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "language switcher")

    def test_zaijs_mirror_list_without_root(self):
        (self.tmp / "public" / "assets" / "js" / "zai.js").write_text(
            'var mirrored = ["/zh/"];\n', encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "lang-switch JS maps every path")

    def test_zaijs_mirror_list_missing_entirely(self):
        (self.tmp / "public" / "assets" / "js" / "zai.js").write_text(
            "// no mirrored list in this build\n", encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "lang-switch JS maps every path")

    def test_search_coverage_missing_page(self):
        (self.tmp / "content" / "zh" / "extra.md").write_text("# Extra\n\nBody.\n", encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "search.json covers all")

    def test_thin_search_snippet(self):
        (self.tmp / "public" / "search.json").write_text(json.dumps(
            [{"u": "/", "s": "short"}, {"u": "/zh/", "s": SNIPPET}]), encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "search entries carry full-body snippets")

    def test_search_client_loses_theme_classes(self):
        (self.tmp / "public" / "assets" / "js" / "search.js").write_text(
            'className = "line-clamp-2"\n', encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "search client emits theme classes")

    def test_missing_404(self):
        (self.tmp / "public" / "404.html").unlink()
        self.assert_fail(self.audit_from_root(), "404.html present")

    def test_rag_archive_with_withheld_bundles(self):
        # The exact regression the content-only RAG decision guards against.
        (self.tmp / "public" / "rag-archive" / "rag-system.md").write_text("internal\n", encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "rag-archive contains only rag-content.md")

    def test_rag_archive_empty(self):
        (self.tmp / "public" / "rag-archive" / "rag-content.md").unlink()
        self.assert_fail(self.audit_from_root(), "rag-archive contains only rag-content.md")

    def test_generated_missing_page_stub_page(self):
        # What the pinned release writes for a dangling internal link.
        (self.tmp / "public" / "ghost").mkdir(parents=True, exist_ok=True)
        (self.tmp / "public" / "ghost" / "index.html").write_text(
            '<html><h3 class="font-bold">🚧 Under Construction</h3>'
            "<div>We are still working on this content. Please check back later!</div></html>",
            encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "no generator missing-page stubs")

    def test_generated_missing_page_stub_node_in_graph(self):
        gd = self.tmp / "public" / "graph" / "data.json"
        data = json.loads(gd.read_text(encoding="utf-8"))
        data["nodes"].append({"id": "ghost", "type": "page", "stub": True, "render": False})
        gd.write_text(json.dumps(data), encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "graph payload marks no missing-page stub nodes")

    def test_sitemap_missing_page(self):
        (self.tmp / "public" / "sitemap.xml").write_text(
            "<urlset><url><loc>https://z.filed.fyi/</loc></url></urlset>", encoding="utf-8")
        self.assert_fail(self.audit_from_root(), "sitemap lists all pages")


class TestEnforcement(unittest.TestCase):
    """The deploy step runs under `set -euo pipefail`; a failing audit must
    end the script before anything that could publish (upload/deploy)."""

    PIPELINE = (
        "set -euo pipefail\n"
        'echo "build steps done" >&2\n'
        'python3 "{audit}"\n'
        'echo "WOULD_UPLOAD" >&2\n'
        'echo "WOULD_DEPLOY" >&2\n'
    )

    def run_pipeline(self, root):
        proc = subprocess.run(
            ["bash", "-c", self.PIPELINE.format(audit=root / "scripts" / "audit-artifact.py")],
            cwd="/", capture_output=True, text=True, timeout=120,
        )
        return proc.returncode, proc.stdout, proc.stderr

    def test_failing_audit_stops_before_upload(self):
        tmp = pathlib.Path(tempfile.mkdtemp(prefix="audit-enforce-"))
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        build_fixture(tmp)
        (tmp / "public" / "rag-archive" / "rag-system.md").write_text("leak\n", encoding="utf-8")
        code, out, err = self.run_pipeline(tmp)
        self.assertNotEqual(code, 0)
        self.assertIn("build steps done", err)
        self.assertNotIn("WOULD_UPLOAD", out + err)
        self.assertNotIn("WOULD_DEPLOY", out + err)
        self.assertIn("rag-archive contains only rag-content.md", out)

    def test_passing_audit_lets_the_pipeline_proceed(self):
        tmp = pathlib.Path(tempfile.mkdtemp(prefix="audit-enforce-"))
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        build_fixture(tmp)
        code, out, err = self.run_pipeline(tmp)
        self.assertEqual(code, 0, out + err)
        self.assertIn("WOULD_UPLOAD", err)


if __name__ == "__main__":
    unittest.main(verbosity=2)
