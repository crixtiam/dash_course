from dash import Dash,html,dcc
#Output Input

from dash.dependencies import Output,Input

import pandas as pd
import numpy as np
import plotly.express as px

#import matplotlib.pyplot as plt
#flask
#https://jvm7rt75-5500.use2.devtunnels.ms/

#body

education = pd.read_csv("./Data/states_all.csv").assign(
    expenditure_per_student = lambda x: x["TOTAL_EXPENDITURE"] / x["GRADES_ALL_G"],
    above_avg_math8 = lambda x: np.where(x["AVG_MATH_8_SCORE"] > 278.6,'Above Avg', 'Below Avg')
)




app = Dash(__name__)

#app.layout = html.Div("hello world")


app.layout = html.Div(
    [
        "Seleccione el país:",
        dcc.Dropdown(
            options=education["STATE"].unique(),
            value=["CALIFORNIA"],
            id='my-dropdown',
            multi=True
        ),
        html.H4(id="id-country"),
        dcc.Graph(id="graph")
    ]
)


@app.callback(
    Output('id-country', 'children'),
    Output("graph","figure"),
    Input("my-dropdown","value")
)
def country_selector(country):
    cadena_texto = f"yo vivo en {country}"
    fig = px.line(
        education.query("STATE in @country and 1992 < YEAR < 2016").reset_index(),
        x = "YEAR",
        y= "AVG_READING_8_SCORE",
        color = "STATE"      
    )

    return cadena_texto,fig

#fin
if __name__=="__main__":
    app.run_server(debug=True,port=8052)



"""

// Filtros
Dropdown
Slider
RangeSlider
Checklist
RadioItems
datePickers

// lo que voy a filtrar en graficas
//Representación gráfica.

Graphs

   boxplot
   histogram
   line
   scatter
"""