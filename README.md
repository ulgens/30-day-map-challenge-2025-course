<div align="center">

# 30-Day Map Challenge 2025 Course Outputs

[comment]: <> (Update ty badge when https://github.com/simple-icons/simple-icons/pull/14138 is merged)

[![Python](https://img.shields.io/badge/python-3.14-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/-uv-DE5FE9?logo=uv&labelColor=555)](https://github.com/astral-sh/uv)
[![prek](https://img.shields.io/badge/-prek-F54327?logo=prek&labelColor=555)](https://github.com/j178/prek)
[![Ruff](https://img.shields.io/badge/-ruff-D7FF64?logo=ruff&labelColor=555)](https://github.com/astral-sh/ruff)
[![Renovate](https://img.shields.io/badge/-renovate-308BE3?logo=renovate&labelColor=555)](https://github.com/renovatebot/renovate)

[![Git Hooks](https://img.shields.io/github/actions/workflow/status/ulgens/30-day-map-challenge-2025-course/git-hooks.yml?logo=github&label=Git%20Hooks)](https://github.com/ulgens/30-day-map-challenge-2025-course/actions/workflows/git-hooks.yml)

</div>

[30-Day Map Challenge 2025: Director's Cut](https://www.udemy.com/share/10eYe73@CqUhOnyIiuypWuOce4upC-lab4bmVikNaqVcdJqnASP_O_HeYBBLlELhNHc6DA==/) (The link may include referrer details.)

## Required tools
- [Copier](https://copier.readthedocs.io/) >= 9.0.0
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [prek](https://prek.j178.dev/installation/)

## Implemented tools & patterns
- [Ruff](https://docs.astral.sh/ruff/): Linting and formatting. Runs as git hooks and in CI. Configuration is in `ruff.toml`.
- [pytest](https://docs.pytest.org/) with [pytest-xdist](https://github.com/pytest-dev/pytest-xdist): Testing with parallel execution. Runs in CI.
- [pyproject-fmt](https://github.com/tox-dev/pyproject-fmt): `pyproject.toml` formatter. Runs as a git hook.
- [yamlfmt](https://github.com/google/yamlfmt): YAML formatter. Runs as a git hook. Configuration is in `yamlfmt.yaml`.
- [codespell](https://github.com/codespell-project/codespell): Spell checker. Runs as a git hook.
- [zizmor](https://github.com/zizmorcore/zizmor): GitHub Actions security auditor. Runs as a git hook.
- [check-jsonschema](https://github.com/python-jsonschema/check-jsonschema): Validates GitHub workflow files and Renovate configuration. Runs as git hooks.
- [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks): General file checks (large files, case conflicts, merge conflicts, TOML/YAML validation, private key detection, trailing whitespace, end-of-file fixer). Runs as git hooks.
- [Renovate](https://docs.renovatebot.com/): Automated dependency updates. Configuration is in `renovate.json5`.

## Contribution
- Install git hooks with `prek install` and ensure your changes pass the checks before creating a pull request.
  - After `prek install`, git hooks will be automatically run while committing. To manually run the checks, use `prek run`.

## Updating the project template

This project was generated from a [Copier](https://copier.readthedocs.io/) template. To pull in the latest changes from the template:

```bash
copier update --trust
```

Resolve any conflicts if prompted. See the [python-anything](https://github.com/ulgens/python-anything) repository for template changelog and details.
