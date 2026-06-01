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

### Linting with `ubc`

The dev container ships the `ubc` CLI, which validates your needs against
`ubproject.toml`:

```bash
ubc
```

> **Note:** `ubc` is free for local development and open source. Running `ubc`
> in CI/CD requires a useblocks *systems license* — see the
> [ubCode docs](https://ubcode.useblocks.com/). This template deliberately does
> not run `ubc` in CI.

---

## License

[MIT](LICENSE) © 2026 uptux
