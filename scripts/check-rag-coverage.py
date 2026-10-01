#!/usr/bin/env python3
"""Prove RAG-export coverage: every content source file, or a recorded exclusion.

The generator's `rag` command writes rag-content.md with one
`<file path="...">` / `<content>` ... `</content>` / `</file>` block per page,
embedding the source file verbatim (frontmatter included). This script:

  1. parses the exported bundle (rag-archive/rag-content.md),
  2. compares its per-file blocks against every markdown file under content/
     (byte-for-byte after unwrapping, whitespace-normalised),
  3. reports the deployed copy (public/rag-archive/rag-content.md) as
     byte-identical or not.

Exits non-zero if any source file is missing from the corpus, if a block
differs from its source, or if the deployed copy drifts from the export.
Intentional exclusions are recorded here as RAG_EXCLUSIONS so a future file
that drops out of the corpus has to be acknowledged, not missed.
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXPORT = ROOT / "rag-archive" / "rag-content.md"
DEPLOYED = ROOT / "public" / "rag-archive" / "rag-content.md"

# Source paths intentionally left out of the RAG corpus, with reasons.
# Empty today: the pinned release embeds all 58 EN/ZH content files.
RAG_EXCLUSIONS: dict[str, str] = {}

BLOCK_RE = re.compile(
    r'^<file path="(?P<path>[^"]+)">\n<content>\n(?P<body>.*?)</content>\n</file>\n?',
    re.S | re.M,
)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    failures = []

    if not EXPORT.is_file():
        print(f"check-rag-coverage: missing export {EXPORT.relative_to(ROOT)}")
        return 1

    export_text = EXPORT.read_text(encoding="utf-8")
    corpus = {m.group("path"): m.group("body") for m in BLOCK_RE.finditer(export_text)}

    sources = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "content").rglob("*.md"))

    missing = [s for s in sources if s not in corpus and s not in RAG_EXCLUSIONS]
    excluded = [s for s in sources if s not in corpus and s in RAG_EXCLUSIONS]
    recorded_but_present = [s for s in RAG_EXCLUSIONS if s in corpus]

    for s in missing:
        failures.append(f"missing from corpus: {s}")
    for s in recorded_but_present:
        failures.append(f"listed as excluded but present in corpus: {s}")

    matched = 0
    for s in sources:
        if s not in corpus:
            continue
        if norm(corpus[s]) != norm((ROOT / s).read_text(encoding="utf-8")):
            failures.append(f"corpus block differs from source: {s}")
        else:
            matched += 1

    if DEPLOYED.is_file():
        if DEPLOYED.read_bytes() == EXPORT.read_bytes():
            deployed = "byte-identical to export"
        else:
            failures.append("public/rag-archive/rag-content.md differs from rag-archive/rag-content.md")
            deployed = "DIFFERS from export"
    else:
        deployed = "not deployed (no public/rag-archive/rag-content.md)"

    print(
        f"check-rag-coverage: {matched}/{len(sources)} source files embedded verbatim; "
        f"{len(excluded)} recorded exclusions; deployed copy {deployed}"
    )
    for s in excluded:
        print(f"  excluded: {s} ({RAG_EXCLUSIONS[s]})")
    for f in failures:
        print(f"  FAIL: {f}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
