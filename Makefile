# Run from this directory. If invoking from a parent directory, pass an
# absolute OUTPUT for the rag target (see docs/HOMESTEAD.md).
LA_FAMILLE ?= la-famille
PROJECT_ROOT ?= .
OUTPUT ?= $(CURDIR)/public/rag-archive

build:
	$(LA_FAMILLE) --project-root $(PROJECT_ROOT) build

check:
	$(LA_FAMILLE) --project-root $(PROJECT_ROOT) check

rag: build
	$(LA_FAMILLE) --project-root $(PROJECT_ROOT) rag --output $(OUTPUT)

publish: build rag
	python3 scripts/strip-internal-nofollow.py
	python3 scripts/enhance-artifact.py
	./scripts/prune-unused-assets.sh
	$(LA_FAMILLE) --project-root $(PROJECT_ROOT) publish-check

.PHONY: build check rag publish
