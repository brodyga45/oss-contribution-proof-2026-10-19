# Python dependency qualification probes

These are existing diagnostic probes from 20 October 2026. They use synthetic data and public library APIs. They demonstrate reproduction and version comparison; they do not implement fixes.

## Panel client-source refresh

From the repository root:

```sh
python3.12 -m venv .venv-panel
.venv-panel/bin/python -m pip install -r qualification/panel-requirements.txt
.venv-panel/bin/python qualification/panel-source.py
.venv-panel/bin/python qualification/panel-requirements.py
```

In the source-refresh probe, appending a fourth row on the same remote page leaves three rows in the Bokeh client data source. The Python DataFrame has four. Local pagination updates, and following onto a new page updates. This checks the model data source, not browser rendering. Public context: [Panel #7721](https://github.com/holoviz/panel/issues/7721).

The requirements probe shows that two imports under the same namespace infer only `plaidcloud`. An explicit requirements list retains both actual distribution names. The imports are parsed without executing those packages. This does not establish their Pyodide compatibility. Public context: [Panel #8565](https://github.com/holoviz/panel/issues/8565).

## Documentation version comparison

From the repository root, create a separate environment:

```sh
python3.12 -m venv .venv-docs
.venv-docs/bin/python -m pip install -r qualification/docs/common-requirements.txt mkdocstrings-python==2.0.8
cd qualification/docs/repro
../../../.venv-docs/bin/python -m mkdocs build --strict --site-dir ../site-2.0.8
../../../.venv-docs/bin/python -m pip install mkdocstrings-python==2.0.9
../../../.venv-docs/bin/python -m mkdocs build --strict --site-dir ../site-2.0.9
```

The first strict build exited 0. The second exited 1 with three unresolved references to private defining-module paths. Only the handler version changed between the two comparison runs. The generated sites are local output, not included here. This is a small synthetic adaptation of [mkdocstrings-python #346](https://github.com/mkdocstrings/python/issues/346), not a complete consumer project or an implemented resolution.

`common-requirements.txt` pins the key comparison dependencies, including pymdown-extensions 11.0.2. An initial setup with pymdown 12 hit a separate highlighting API error before the comparison; those results were not treated as the reported cross-reference regression.

## Scope and provenance

[observations.json](observations.json) records the narrow observations. A commissioned fix still needs agreed target versions, intended behavior and acceptance checks. See [the maintenance offer](../COMMISSIONING.md).

Original probes prepared by brodyga45 with OpenAI Codex. No human review, accepted upstream contribution, customer history or payment is claimed. AGPL-3.0-only; see [NOTICE](NOTICE) and the repository LICENSE. Dependencies retain their own licenses.
