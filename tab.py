import pandas as pd
from dash import Dash,dcc,html
import plotly.express as px

#callback
from dash.dependencies import Output,Input
from dash.exceptions import PreventUpdate


app = Dash(__name__)


lista_elementos=[
    html.H1("Dashboard de comidas"),
    dcc.Tabs(
        id='tabs',
        value="Tab-1",
        className="dbc",
        children=[
            dcc.Tab(
                label="tab-pricipal",
                value="Tab-1",
                className="dbc",
                children=[
                    html.H1("Estoy en el tab 1")
                ]
            ),
             dcc.Tab(
                label="tab-pricipal",
                value="Tab-2",
                className="dbc",
                children=[
                    html.H1("Estoy en el tab 2")
                ]
            ),
            dcc.Tab(
                label="tab-pricipal",
                value="Tab-3",
                className="dbc",
                children=[
                    html.H1("Estoy en el tab 3")
                ]
            )
        ]
    )
]



app.layout = html.Div(
   lista_elementos
)


if __name__=="__main__":
    app.run_server(port=8055,debug=True)