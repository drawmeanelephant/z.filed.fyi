#!/usr/bin/env python3
"""Strip rel="nofollow" from internal links in the publish artifact.

The generator's markdown sanitizer stamps rel="nofollow" on every rendered
link. For a small editorial site that is the wrong signal on its own
navigation, and it hurts internal link architecture. External links keep the
sanitizer default; internal links (relative, root-relative, or fragment) get
the attribute removed. Idempotent. Run between build and publish-check in
`make publish`.
"""
import pathlib
import re

PUB = pathlib.Path(__file__).resolve().parent.parent / "public"
TAG_RE = re.compile(r"<a\b[^>]*>", re.I)
HREF_RE = re.compile(r'href="([^"]*)"', re.I)
REL_RE = re.compile(r'\s+rel="nofollow"', re.I)


def is_external(href):
    if href.startswith("#"):
        return False
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:", href) or href.startswith("//"))


def main():
    cleaned = files = 0
    for p in PUB.rglob("*.html"):
        text = p.read_text(encoding="utf-8")
        files += 1

        def fix(m):
            nonlocal cleaned
            tag = m.group(0)
            if "nofollow" not in tag.lower():
                return tag
            hm = HREF_RE.search(tag)
            if not hm:
                return tag
            if is_external(hm.group(1)):
                return tag
            new = REL_RE.sub("", tag)
            if new != tag:
                cleaned += 1
            return new

        new_text = TAG_RE.sub(fix, text)
        if new_text != text:
            p.write_text(new_text, encoding="utf-8")
    print(f"strip-internal-nofollow: cleaned {cleaned} links in {files} html files")


if __name__ == "__main__":
    main()
