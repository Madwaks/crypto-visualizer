import dash_core_components as dcc
import dash_html_components as html

from crypto_viz import settings

layout = html.Div([
    html.Label('Symbol'),
    dcc.Dropdown(
        id="symbol_select",
        options=[{"label": symbol.get("name"), "value": symbol.get("name")} for symbol in settings.symbols],
        value="ETHBTC",
    ),
    html.Div(id='graph', children=dcc.Graph(id='symbol_quotes_graph')),
    html.Label('Moving averages'),
    dcc.Checklist(id="indicators_list",
                  options=settings.INDICATORS_CHECKLIST, labelStyle=settings.STYLE_MM_CHECKLIST
                  ),
    html.Label("Support & Resistances"),
    dcc.Checklist(id="key_levels",
                  options=[{"label": "Yes", "value": "True"}], labelStyle=settings.STYLE_MM_CHECKLIST
                  )
])
