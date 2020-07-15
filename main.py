# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:41:58 2020

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

#data collection part__________________________________________________________


total_confirmed,sorted_confirmed,total_deaths,sorted_death,total_recovered,sorted_recovered,top_25_cities=tweets_analyse.get_data()
time_series_df=tweets_analyse.time_series_creation()

#read sentiment data
sentiment_values,sentimet_names,emotion_value,emotion_name,future_sentiment_value,future_sentimet_names,total=sentiment_data.get_sentiment_data()


colors={
        'background':'black',
        
        }
#total count of deatha and confirmed cases
total=[total_confirmed,total_deaths,total_recovered]
total_name=['    -  Global confirmed','     -   Global Death','     -   Global Recovery']

#sorted cases among the country

#generate scrolabel data for death and confirm cases
def generate_tabel(df,title):
    return html.Table([

        html.Caption(title),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
                ]) for i in range(len(df))
            ])
        ])


#map creation__________________________________________________________________
    
#access token from mapbox https://account.mapbox.com/
token='pk.eyJ1IjoibmluamFhYyIsImEiOiJja2J5bjB4YmQwaXg2MzBuNHNzaTA0bXk2In0.BVaAwyDqBSPCCYqRFQBdcA'   

fig = px.scatter_mapbox(time_series_df, 
                        lat="Lat", lon="Long", 
                        hover_name="Country/Region", 
                        hover_data=['Country/Region'],
                        zoom=1,
                        color_discrete_sequence=["fuchsia"],
                        height=500)

fig.update_layout(mapbox_style="dark",mapbox_accesstoken=token)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#time series map ceration based on the map cover data____________________________________
colors={
    'backgroud':"black",
    'text':'gray',
}
def create_time_series(df,country_name,col_name,title):
    fig=dict(
        data=[
            {'x':list(df['date']), 'y':list(df[col_name]),
             'type' : 'bar' ,
             'name' : 'Date',
             'color':['red'],
                 },
            ],
        layout={'title' : country_name +'\t' + title,
                
                'plot_bgcolor':colors['backgroud'],
                'paper_bgcolor':colors['backgroud'],
                'font' :{
                    'color':colors['text']  
                    },
                'height':350,
                },
        )
    
    return fig
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
# future sentiment pie chart making______________________________________________________________

def generate_pie_future_graph(future_sentiment_value,future_sentimet_names,colors):
    fig_pie_future = px.pie(
                values=future_sentiment_value,
                names=future_sentimet_names,
                color_discrete_sequence=['#66004d','green','#b30086'],
                opacity=0.9,
                hole=0.7,
                
              )

    fig_pie_future.update_traces(  marker_line_color='red',
                        textposition='inside', 
                        textinfo='percent')
    fig_pie_future.update_layout(
                        clickmode='event+select',
                        margin={},
                        plot_bgcolor=colors['backgroud'],
                        paper_bgcolor=colors['backgroud'],
                        font ={
                                'color':colors['text']  
                                },                        
                        height=350,
                        )
    return fig_pie_future

#bar chart for emotion analysis________________________________________________
def generate_bar_graph(emotion_value,emotion_name,colors):
    fig_bar=px.bar(
                x=emotion_value,
                y=emotion_name,
                text=emotion_value,
                color_discrete_sequence=['#66004d'],
                labels={'x':'','y':''},
                opacity=0.7
                )
    fig_bar.update_traces(
                        texttemplate='%{text:.2s}',
                        textposition='outside'
                        )
    fig_bar.update_layout(uniformtext_minsize=8
                          ,uniformtext_mode='hide',
                          font={'color':'gray'})
    fig_bar.update_layout(
                        margin={},
                         plot_bgcolor=colors['backgroud'],
                        paper_bgcolor=colors['backgroud'],
                        height=350,
                        )
    return fig_bar

#morality line graph_____________________________________________________________________________
fig_line=dict(
        data=[
            {'x':top_25_cities['Country_Region'], 'y':top_25_cities['Mortality Rate (per 100)'],
             'type' : 'lines+markers' ,

             'color':"['red']",
             'color_discrete_sequence':"['red']"
                 },
            ],
        layout={'title' :'Top 25 Mortality rate of cities ',
                
                'plot_bgcolor':colors['backgroud'],
                'paper_bgcolor':colors['backgroud'],
                'font' :{
                    'color':colors['text']  
                    },
                'markers':{'linecolor':'red'},
                
                
                },
        )
#generate the morality details from the hoverdata_______________________________________________________
def generate_morality_details(country_name):
    df=top_25_cities[top_25_cities['Country_Region'] == country_name]
    mor=df['Mortality Rate (per 100)']
    total_death=df['Deaths']
    total_confirmed=df['Confirmed']
    for i in total_death:
        total_death=str(i)
    for j in total_confirmed:
        total_confirmed=str(j)
    for m in mor:
        mor=str(m)
    
    return [
            html.H2('Mortality details of '+ '\t' + country_name),
            html.P('Mortality rate also called Death rate,is a measure of the number of death  scaled to the size of the population '),
            html.H4('Total deaths yesterday  :'+'\t' + total_death),
            html.H4('Total confirmed cases yesterday  :'+'\t' + total_confirmed),
            html.H1(mor)
        ]

#style for tab backgroud_____________________________________________________________________

tab_selected_style = {
    
    
    'backgroundColor': 'black',
    'color': 'white',
    'padding': '6px'
}
#dash app starts____________________________________________________________________________

app=dash.Dash(__name__,)

print('helo hey')
app.title='Covid19 DashBoard'
app.layout=html.Div(children=[
                    
                    html.Div(className='header',
                                                 
                            style={'textAlign':'center',
                                   'display':'inline-block',
                                   },
                            children=[html.H1('Covid19 Dashboard - Sentiment and Emotion'),
                                      html.A('Contact our CovidBot',href='https://node-red-qygur.eu-gb.mybluemix.net/ui/#!/0?socketid=adN3jIShls3mUdSoAAAE',target='_block'),]),
                                       

                                      

                    html.Div(className='first_box',
                             style={'width':'17%',
                                    'display':'inline-block',
                                    'float':'left'},
                             children=[html.Ol(id='total_list',children=[html.Li(html.Div(style={'height':'30px'},className='list',children=[html.H2(i),html.H6(j)])) for i,j in zip(total,total_name)])
                                       ]),
                    
                    html.Div(className='confirm_countrywise',
                             style={'width':'17%',
                                    'display':'inline-block,',
                                    'float':'right'},
                             children=[generate_tabel(sorted_confirmed,"Total Confirmed cases"),
                                       
                                       ]),

                    html.Div(className='sentiment_emotion_graph',
                             style={'width':'64%',
                                    'display':'inline-block',
                                    'float':'right',},
                             children=[     
                                 dcc.Tabs(
                                     parent_className='custom-tabs',
                                     className='custom-tabs-container',
                                     children=[
                                     dcc.Tab(label='Sentiment of people duirng COVID19 lockdown', 
                                            className='custom-tab',
                                            selected_style=tab_selected_style,
                                            selected_className='custom-tab--selected',
                                            
                                            children=[
                                 
                                     html.Div(className='sentiment_pie',
                                              style={'width':'90%',
                                                     'display':'inline-block',
                                                     'float':'left'},
                                                children=[
                                                    dcc.Graph(id='sentiment_pie_chart'),
                                                    dcc.Interval(
                                                                  id='interval_pie',
                                                                  interval=1*5000,
                                                                  n_intervals=0),
                                                    
                                                    
                                         ]) ]),
                                    
                                    dcc.Tab(label='Sentiments, If lockdown Extended', 
                                            className='custom-tab',
                                            selected_style=tab_selected_style,
                                            selected_className='custom-tab--selected',                                            
                                            
                                            
                                            children=[
                                 
                                     html.Div(className='sentiment_pie',
                                                 style={'width':'90%',
                                                       'display':'inline-block',
                                                       'float':'left'},
                                                children=[
                                                    dcc.Graph(id='future_sentiment_pie_chart',),
                                                    dcc.Interval(
                                                        id='interval_pie_future',
                                                        interval=1*5000,
                                                        n_intervals=0,
                                                        ),
                                                    
                                         ]) ]),
                                    dcc.Tab(label='Emotions of people during COVID19 lockdown', 
                                            className='custom-tab',
                                            selected_style=tab_selected_style,
                                            selected_className='custom-tab--selected',                                            
                                            
                                            children=[
                                       html.Div(className='emotion_bar',
                                                 style={'width':'90%',
                                                       'display':'inline-block',
                                                       'float':'right'},  
                                                 children=[
                                                     dcc.Graph(id='emotion_bar_chat',),
                                                     dcc.Interval(
                                                         id='interval_bar_emotoin',
                                                         interval=1*5000,
                                                         n_intervals=0,
                                                         ),
                                                     html.Div(id='sentiment_clickdata')
                                                     ]
                                                )
                                 ])],colors={"background": "black"},
                                    
                                    
                                    )]),

                    html.Div(className='death_countrywise',
                             style={'width':'17%',},
                             children=[generate_tabel(sorted_death,'Total Death In Counties'),
                                      ]
                             ) ,
                    html.Div(className='death_countywise_name',
                             style={"width":"17%",},
                             children=[html.Div('Death Basedon Country')]),
                                       
                    html.Div(className='map',
                             style={'width':'60%',
                                    'display':'inline-block',
                                    'height':'5%',
                                    'float':'left'},
                             children=[
                                
                                     dcc.Graph(
                                             id='scatter_world_map',
                                             hoverData={'points':[{'customdata':['India']}]},
                                             figure=fig,
                                                )
                                 ]),
                    html.Div(className='time_series_map',
                             style={'dispaly':'inline-block',
                                    'width':'38%',
                                    "float":'right'},
                             children=[
                                 dcc.Graph(
                                     id='death_time_series_map',
                                     ),
                                 dcc.Graph(
                                     id='conifrm_time_series_map',
                                     )
                                 ]),
                    html.Div(className='morality_line_mark',
                             style={'display':'inline-block',
                                    'width':'60%',
                                    'float':'left'},
                             children=[
                                 dcc.Graph(
                                             id='morality_line_mark',
                                             figure=fig_line,
                                             hoverData={'points':[{'x':'Yemen'}],}
                                             
                                     ),
                                     
                                             
                                 ]),
                    html.Div(
                                     
                                className='morality_details',
                                id='morality_details',
                                style={
                                        'display':'inline-block',
                                        'width':'38%',
                                        'float':'right',
                                                 },
                                children=[]),
                   
                   
                        
                        ])

"""
@app.callback(Output(component_id='check', component_property='children'),
              [Input(component_id='scatter_world_map',component_property='hoverData')])
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)

"""

#call pack starts_______________________________________________________________________________


@app.callback(Output(component_id='sentiment_pie_chart',component_property='figure'),
              [Input(component_id='interval_pie',component_property='n_intervals')])
   
def update_pie_graph(n):
    colors={
        'backgroud':"black",
        'text':'gray',
    }
    print('hello pie sentiment updated')
    sentiment_values,sentimet_names,emotion_value,emotion_name,future_sentiment_value,future_sentimet_names,total=sentiment_data.get_sentiment_data()
    return generate_pie_sentimnet_graph(sentiment_values,sentimet_names,colors)

@app.callback(Output(component_id='future_sentiment_pie_chart',component_property='figure'),
              [Input(component_id='interval_pie_future',component_property='n_intervals')])

def update_future_pie_graph(n):
    colors={
        'backgroud':"black",
        'text':'gray',
    }
    print('hello pie sentiment future updated')
    sentiment_values,sentimet_names,emotion_value,emotion_name,future_sentiment_value,future_sentimet_names,total=sentiment_data.get_sentiment_data()
    return generate_pie_future_graph(future_sentiment_value,future_sentimet_names,colors)   
   
@app.callback(Output(component_id='emotion_bar_chat',component_property='figure'),
              [Input(component_id='interval_bar_emotoin',component_property='n_intervals')])

def update_bar_graph(n):
    colors={
        'backgroud':"black",
        'text':'gray',
    }
    print('hello bar emotion updated')
    sentiment_values,sentimet_names,emotion_value,emotion_name,future_sentiment_value,future_sentimet_names,total=sentiment_data.get_sentiment_data()
    return generate_bar_graph(emotion_value,emotion_name,colors)   
   
 
@app.callback(Output(component_id='death_time_series_map', component_property='figure'),
              [Input(component_id='scatter_world_map',component_property='hoverData')])
def ubdate_death_time_series(hoverData):
    #full=full_table_f[full_table_f['Country/Region'] == 'Afghanistan']
    country_name = hoverData['points'][0]['customdata'][0]
    time_df=time_series_df[time_series_df['Country/Region'] == country_name]
    time_df_death=time_df[['Death','date']]
    col_name='Death'
    title='Death rate Date wise'
    return create_time_series(time_df_death,country_name,col_name,title)
    

@app.callback(Output(component_id='conifrm_time_series_map', component_property='figure'),
              [Input(component_id='scatter_world_map',component_property='hoverData')])
def ubdate_confirm_time_series(hoverData):
    #full=full_table_f[full_table_f['Country/Region'] == 'Afghanistan']
    country_name = hoverData['points'][0]['customdata'][0]
    time_df=time_series_df[time_series_df['Country/Region'] == country_name]
    time_df_death=time_df[['Confirmed','date']]
    col_name='Confirmed'
    title='Confirm cases Date wise'
    return create_time_series(time_df_death,country_name,col_name,title)

   
@app.callback(Output(component_id='morality_details',component_property='children'),
              [Input(component_id='morality_line_mark',component_property='hoverData')])
def display_morality_details(hoverData):
    country_name = hoverData['points'][0]['x']
    return generate_morality_details(country_name)

#run dash app______________________________________________________________________________________________
  
if __name__=='__main__':
    app.run_server(debug=True)

