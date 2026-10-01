# Run from this directory. If invoking from a parent directory, pass an
# absolute OUTPUT for the rag target (see docs/HOMESTEAD.md).
LA_FAMILLE ?= la-famille
PROJECT_ROOT ?= .
OUTPUT ?= $(CURDIR)/rag-archive

build:
	$(LA_FAMILLE) --project-root $(PROJECT_ROOT) build

check:
	$(LA_FAMILLE) --project-root $(PROJECT_ROOT) check

# The RAG export lands outside public/ on purpose: the generator writes a
# content bundle plus rag-system.md (repo workflows, README) and rag-config.md
# (a full file inventory), and only the content bundle is publishable.
rag: build
	$(LA_FAMILLE) --project-root $(PROJECT_ROOT) rag --output $(OUTPUT)

publish: build rag
	mkdir -p public/rag-archive
	cp rag-archive/rag-content.md public/rag-archive/rag-content.md
	python3 scripts/strip-internal-nofollow.py
	python3 scripts/enhance-artifact.py
	./scripts/prune-unused-assets.sh
	$(LA_FAMILLE) --project-root $(PROJECT_ROOT) publish-check
	python3 scripts/check-rag-coverage.py

.PHONY: build check rag publish
