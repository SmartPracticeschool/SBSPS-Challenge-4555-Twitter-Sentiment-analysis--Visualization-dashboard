# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:18:06 2020

@author: ninjaac
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer
from dash.dependencies import Input,Output
import pandas as pd

from tweetwrangling import tweets_analyse

from node_red_data_collection import sentiment_data
import json
import plotly.express as px
import plotly.graph_objects as go

#sentiment pie chart making______________________________________________________________
def generate_pie_sentimnet_graph(sentiment_values,sentimet_names,colors):
    fig_pie = px.pie(
                values=sentiment_values,
                names=sentimet_names,
                color_discrete_sequence=['#66004d','green','#b30086'],
                opacity=0.9,
                hole=0.7,
                
              )

    fig_pie.update_traces(  marker_line_color='red',
                        textposition='inside', 
                        textinfo='percent')
    fig_pie.update_layout(  clickmode='event+select',
                        margin={},
                        plot_bgcolor=colors['backgroud'],
                        paper_bgcolor=colors['backgroud'],
                        font ={
                                'color':colors['text']  
                                },                        
                        height=350,
                        )
    return fig_pie

app = dash.Dash(__name__)

app.layout = html.Div(
    html.Div([


        dcc.Graph(id='sentiment_pie_chart'),
        dcc.Interval(
            id='interval_component',
            interval=1*10000,
            n_intervals=0
        )
    ])
)

@app.callback(Output(component_id='sentiment_pie_chart',component_property='figure'),
              [Input(component_id='interval_component',component_property='n_intervals')])

def update_pie_graph(n):
    colors={
        'backgroud':"black",
        'text':'gray',
    }
    print("hello")
    sentiment_values,sentimet_names,emotion_value,emotion_name,future_sentiment_value,future_sentimet_names,total=sentiment_data.get_sentiment_data()
    return generate_pie_sentimnet_graph(sentiment_values,sentimet_names,colors)   
 
#run dash app______________________________________________________________________________________________
  
if __name__=='__main__':
    app.run_server(debug=True)
