# Makefile for the Sphinx-Needs Starter template.
# Commands run through `uv run` so the project's pinned tools are used.

SOURCEDIR = source
BUILDDIR  = build

.PHONY: help html ubtrace serve clean

# Default target: show available commands.
.DEFAULT_GOAL := help

help:  ## List available targets
	@echo "Available targets:"
	@echo "  help     Show this help (default)"
	@echo "  html     Build the HTML docs into $(BUILDDIR)/html"
	@echo "  ubtrace  Build the ubtrace output into $(BUILDDIR)/ubtrace"
	@echo "  serve    Live preview with auto-rebuild on http://localhost:8000"
	@echo "  clean    Remove the $(BUILDDIR) directory"

html:  ## Build the HTML documentation
	uv run sphinx-build -b html "$(SOURCEDIR)" "$(BUILDDIR)/html"

ubtrace:  ## Build the ubtrace output
	uv run sphinx-build -b ubtrace "$(SOURCEDIR)" "$(BUILDDIR)/ubtrace"

serve:  ## Live preview with auto-rebuild (port 8000)
	uv run sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)/html"

clean:  ## Remove build artifacts
	rm -rf "$(BUILDDIR)"
