# sphinx-needs-starter

A ready-to-build documentation environment for [Sphinx](https://www.sphinx-doc.org/)
+ [Sphinx-Needs](https://sphinx-needs.readthedocs.io/) (8.x), with the
[useblocks](https://useblocks.com/) toolchain wired in: the `ubc` validator, and
both the **HTML** and **ubTrace** builders. It ships a dev container and a
[uv](https://docs.astral.sh/uv/)-managed environment so the whole thing builds
the moment you open it.

> **Use it as a base:** click **“Use this template”** on GitHub, or just clone
> this repository. Drop your `.rst` files into `source/`, build, and you're
> good to go.

---

## What's in the box

| Piece | What it does |
| --- | --- |
| **uv** | Pins and installs the Sphinx toolchain (`uv sync`). Non-package project — there's nothing to build but the docs. |
| **Dev container** | Python 3.12 + uv + the `ubc` CLI, plus the right VS Code extensions, preconfigured. |
| **Sphinx-Needs 8.x** | Requirements/specs/tests as first-class, traceable objects. |
| **Furo theme** | Clean, responsive HTML output. |
| **HTML builder** | `make html` → browsable docs. |
| **ubTrace builder** | `make ubtrace` → structured output for [ubTrace](https://ubtrace.useblocks.com/). |
| **`ubproject.toml`** | Single source of truth for need types, shared by `ubc` (lint) and the Sphinx build. |
| **Diagrams** | Graphviz, PlantUML, and Mermaid render during the build — toolchain preinstalled in the dev container. See `source/diagrams.rst`. |

---

## Quick start — Dev container (recommended)

Requires [Docker](https://www.docker.com/) and VS Code with the
**Dev Containers** extension.

1. Open this folder in VS Code.
2. **Reopen in Container** when prompted (or run *Dev Containers: Reopen in
   Container*). The container builds Python 3.12, uv, and the `ubc` CLI, then
   runs `uv sync` automatically.
3. Build the docs:

   ```bash
   make html
   ```

   Open `build/html/index.html`.

For a live-reloading preview while you write:

```bash
make serve     # http://localhost:8000
```

## Quick start — Local (no container)

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/) and
Python 3.12.

```bash
uv sync                          # create .venv with the toolchain
./.devcontainer/install-ubc.sh   # optional: install the ubc CLI on your host
make html                        # build the HTML docs
```

> **Diagrams on a bare host:** Graphviz and PlantUML render at build time, so
> install `graphviz` (the `dot` binary) and `plantuml` (needs Java) on your
> host. The dev container already includes both. Mermaid needs nothing extra.

---

## Add your documentation

1. Put your `.rst` files in **`source/`**.
2. Wire them into the `toctree` in `source/index.rst` (one document name per
   line, without the `.rst` extension).
3. Rebuild: `make html`.

Sphinx-Needs directives (`.. req::`, `.. spec::`, `.. test::`, `.. needtable::`,
…) work out of the box — see `source/index.rst` for a minimal example and the
[Sphinx-Needs docs](https://sphinx-needs.readthedocs.io/) for the full set.

---

## Customize

Three files hold the values you'll want to make your own:

- **`source/conf.py`** — project name/author, and the three `ubtrace_*` settings
  (`ubtrace_organization`, `ubtrace_project`, `ubtrace_version`). Look for the
  `← customize` markers.
- **`ubproject.toml`** — your project name and your **need types** (`req`,
  `spec`, `test`, …). This file is read by both `ubc` and the Sphinx build, so
  the two never drift apart.
- **Versions to bump** when you want to move forward:
  - `sphinx-needs` and the rest of the toolchain → edit `pyproject.toml`, then
    `uv lock --upgrade && uv sync`.
  - The `ubc` CLI → the `UBC_VERSION` arg in `.devcontainer/devcontainer.json`
    (and `.devcontainer/Dockerfile`).

---

## Build commands

| Command | Result |
| --- | --- |
| `make html` | Build HTML docs into `build/html/` |
| `make ubtrace` | Build ubTrace output into `build/ubtrace/` |
| `make serve` | Live preview with auto-rebuild on http://localhost:8000 |
| `make clean` | Remove `build/` |

All targets run through `uv run`, so they use the pinned toolchain whether or
not the venv is activated.

### `ubc` and VS Code tasks

The dev container ships the `ubc` CLI, which works against `ubproject.toml`.
Ready-made **VS Code tasks** are in `.vscode/tasks.json` (run them via
*Terminal → Run Task…*):

| Task | Command | License? |
| --- | --- | --- |
| `ubc: build needs.json` | `ubc build needs . --outpath build/needs.json` | not required |
| `ubc: validate needs.json` | `ubc build validate-json build/needs.json` | not required |
| `ubc: index (report warnings)` | `ubc build index --show-warnings` | not required |
| `ubc: check current file` | `ubc check <file>` | **required** |
| `ubc: check project` | `ubc check source` | **required** |
| `ubc: schema validate` | `ubc schema validate` | **required** |
| `docs: build html` / `ubtrace` / `serve` / `clean` | `make …` | — |

> **Licensing.** The `build` commands (needs export, indexing, JSON validation)
> run with no license. `ubc check` and `ubc schema validate` require a ubCode
> license — **free for open source**, but the project must be recognized as an
> open-source repo (public, OSI license) or you must configure a license key.
> See the [ubCode docs](https://ubcode.useblocks.com/). Running `ubc` in CI/CD
> needs a *systems license*; this template does not run `ubc` in CI.

> **Note on diagrams:** `ubproject.toml` lists PlantUML's `uml` directive under
> `parse.ignore_directives` so `ubc` doesn't flag it as unknown (Sphinx renders
> it). Graphviz, Mermaid, and Sphinx-Needs directives are recognized natively.

---

## License

[MIT](LICENSE) © 2026 Patrick Dahlke
