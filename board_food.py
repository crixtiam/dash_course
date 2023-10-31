import pandas as pd
from dash import Dash,dcc,html
import plotly.express as px

#callback
from dash.dependencies import Output,Input
from dash.exceptions import PreventUpdate


data = pd.read_csv("./Data/fastfood_calories.csv",sep=",")


print(data.dtypes)

###################################################################################

data = data.rename(
    columns={"item":"productos","calories":"calorias"}
)

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



###################################################################################
print(data.head(20))


app = Dash(__name__)


app.layout= html.Div(
    [
        html.H1("Dashboard de comidas"),
        html.H2("Este es un subtitulo "),
        html.P(id="id-parrafo"),
        dcc.Dropdown(options=data.restaurant.unique(),id="id-dropdown",multi=True),
        dcc.Graph(id='graph'),
        #flask

    ]
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
            hover_data="restaurant",
            size="sat_fat",
            title=f"{restaurant} Calories and sugar"


        )

    return text,fig

if __name__=="__main__":
    app.run_server(port=8054,debug=True)
