"""Presales reproduction only: four synthetic Tabulator stream controls."""

import socket

import pandas as pd
import panel as pn

pn.extension("tabulator")


def make_case(label, pagination, page_size, follow):
    table = pn.widgets.Tabulator(
        pd.DataFrame({"name": ["Alice", "Bob", "Charlie"], "n": [1, 2, 3]}),
        pagination=pagination,
        page_size=page_size,
        height=195,
        sizing_mode="stretch_width",
    )
    state = pn.pane.Markdown("Python rows: **3**; stream calls: **0**")
    button = pn.widgets.Button(name=f"Append Delta: {label}", button_type="primary")

    def append_once(event):
        table.stream({"name": ["Delta"], "n": [4]}, follow=follow)
        state.object = f"Python rows: **{len(table.value)}**; stream calls: **1**; page: **{table.page}**"
        button.disabled = True

    button.on_click(append_once)
    return pn.Column(
        pn.pane.Markdown(f"### {label}"), button, state, table,
        sizing_mode="stretch_width",
    )


def make_app():
    return pn.Column(
        pn.pane.Markdown(
            f"# Tabulator streaming: browser qualification\n"
            f"Panel {pn.__version__}, pandas {pd.__version__}. "
            "Synthetic local data; unchanged library; no client records. "
            "Click each append button once and inspect the rendered rows."
        ),
        pn.GridBox(
            make_case("local / size 10 / follow true", "local", 10, True),
            make_case("remote / size 10 / follow true", "remote", 10, True),
            make_case("remote / size 3 / follow true", "remote", 3, True),
            make_case("remote / size 10 / follow false", "remote", 10, False),
            ncols=2,
            sizing_mode="stretch_width",
        ),
        sizing_mode="stretch_width",
    )


if __name__ == "__main__":
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
    print(f"LOCAL_PROBE_URL=http://127.0.0.1:{port}/", flush=True)
    pn.serve(
        make_app,
        address="127.0.0.1",
        port=port,
        websocket_origin=[f"127.0.0.1:{port}"],
        show=False,
    )
