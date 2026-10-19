import json
import platform
import panel as pn
import pandas as pd
from bokeh.document import Document

pn.extension("tabulator")
results = []
for pagination, page_size, follow in [("local", 10, True), ("remote", 10, True), ("remote", 3, True), ("remote", 10, False)]:
    table = pn.widgets.Tabulator(pd.DataFrame({"name": ["Alice", "Bob", "Charlie"], "n": [1, 2, 3]}), pagination=pagination, page_size=page_size)
    model = table.get_root(Document())
    before = {k: list(v) for k, v in model.source.data.items()}
    table.stream({"name": ["Delta"], "n": [4]}, follow=follow)
    after = {k: list(v) for k, v in model.source.data.items()}
    results.append({"pagination": pagination, "page_size": page_size, "follow": follow, "page_after": table.page, "python_rows_after": len(table.value), "client_source_before": before, "client_source_after": after, "delta_in_client_source": "Delta" in after["name"]})
print(json.dumps({"panel": pn.__version__, "pandas": pd.__version__, "python": platform.python_version(), "platform": platform.platform(), "scope": "Bokeh client-source model only; no browser or server session; no fix implemented", "cases": results}, indent=2, default=str))
