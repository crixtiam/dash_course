import pandas as pd
from dash import Dash,dcc,html
import plotly.express as px

#callback
from dash.dependencies import Output,Input
from dash.exceptions import PreventUpdate

import dash_table as dt

####################
# Lectura de datos
####################

data = pd.read_csv("./Data/fastfood_calories.csv",sep=",")


print(data.dtypes)

###################################################################################

data = data.rename(
    columns={"item":"productos","calories":"calorias"}
)

print(data.columns)

def categorize_products(food_item):
    food_item = food_item.lower()
    if "burger" in food_item:
        return "Burguer"
    elif "pizza" in food_item:
        return "Pizza"
    elif "nuggets" in food_item:
        return "Nuggets"
    elif "dog" in food_item:
        return "Hotdog"
    elif "salad" in food_item:
        return "Salad"
    elif "wrap" in food_item:
        return "Wrap"
    else:
        return "Otros"
    


data["categorias_productos"] = data["productos"].apply(categorize_products)


###########################################################################################

app = Dash(__name__)

style_color = {
    "font-family":"cursive",
    "background-color": "#00b36b",
    "color":"white",
    "horizontal-align":"center",
    "text-align":"center",
    "width":"auto"
}





lista_elementos_tab=[
    dcc.Tabs(
        id='tabs',
        value="Tab-1",
        className="dbc",
        children=[
            dcc.Tab(
                label="Dispersión variables",
                value="Tab-1",
                className="dbc",
                children=[
                    #html.H1("Dashboard de comidas"),
                    #html.H2("Este es un subtitulo "),
                    html.P(id="id-parrafo"),
                    dcc.Dropdown(options=data.restaurant.unique(),id="id-dropdown",multi=True),
                    dcc.Graph(id='graph'),
                    #html.H1("Estoy en el tab 1")
                ]
            ),
             dcc.Tab(
                label="tab-pricipal",
                value="Tab-2",
                className="dbc",
                children=[
                    html.P(id="id-parrafo-tab2"),
                    dcc.Dropdown(options=data.restaurant.unique(),id="id-dropdown-tab2",multi=True),
                ]
            ),
            dcc.Tab(
                label="tab-pricipal",
                value="Tab-3",
                className="dbc",
                children=[
                    html.H1("Estoy en el tab 3"),
                    dt.DataTable(id='tbl', data=data.to_dict('records'),columns=[{"name": nombre_columna, "id": nombre_columna} for nombre_columna in data.columns])
                ]
            )
        ]
    )
]





children = [
        html.Div(
            style=style_color,
            children=[
            html.H1("Welcome to my food-dashboard"),
            html.P("En este dashboard se podran visualizar métricas sobre las comidas rápidas")
            ]
            ),
        
        html.Div(
            lista_elementos_tab
        )
    ]









### DIV PRINCIPAL
app.layout = html.Div(
    children=children

)


@app.callback(
    Output('id-parrafo','children'),
    Output("graph","figure"),
    Input('id-dropdown', 'value'),
    #Input("id-checkbox","value_check")
)
def board(restaurant):
    if not restaurant:
        raise PreventUpdate
    else:
        text = f"El restaurante seleccionado es {restaurant}"
        fig = px.scatter(
            data_frame=data.query("restaurant in @restaurant"),
            x="calorias", y="sugar",
            color="categorias_productos",
            hover_data=["restaurant","productos"],
            size="sat_fat",
            title=f"{restaurant} Calories and sugar",
            marginal_x="box",
            marginal_y="box",
        )

    return text,fig



if __name__=="__main__":
    app.run_server(port=8055,debug=True)