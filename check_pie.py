# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:32:43 2020

@author: ninjaac
"""


from node_red_data_collection import sentiment_data
import json
import plotly.express as px
import plotly.graph_objects as go

tweet_df,sentiment_df,emotion_df=sentiment_data.get_sentiment_data()

fig_pie = px.pie(sentiment_df, values='sentiment',
             title='Sentiment of peoples',
              )

fig_pie.update_traces(textposition='inside', textinfo='percent+label')

fig_pie.update_layout(
    margin={'l':5 ,'r':5 ,'b':5 ,'t':10,'pad':10},
    plot_bgcolor='black',
    paper_bgcolor='black',
    height=150,
    )
fig_pie.show()

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:28:06 2020

@author: ninjaac
"""


import plotly.express as px
df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')
fig.show()
import pandas as pd
import numpy as np
fileurl = r'F:\dash_app\dash_ibm_app\dataset\covid19_daily.csv'
df = pd.read_csv(fileurl)
df.to_html(r'F:\dash_app\dash_ibm_app\dataset\time_seris_global_conformed.html')

req_columns = ['Country_Region','Confirmed','Deaths','Recovered','Active']
df_filtered = df[req_columns].copy()
df_filtered.head()
#groupby country names 

df_consolidated = df_filtered.groupby(by='Country_Region',as_index=False).sum()
df_consolidated.head()

#getting states morality rate it  is the value that is divide death by total confirmed cases
#morality high means death is high

df_consolidated["Mortality Rate (per 100)"] = np.round(100*df_consolidated["Deaths"]/df_consolidated["Confirmed"],2)
morality_df=df_consolidated[['Mortality Rate (per 100)','Country_Region','Deaths','Confirmed']].copy()

for i in range(len(morality_df)):
    list=[morality_df.iloc[i,:]]
    df=pd.DataFrame(list)
    print(df)
    df.to_html(r'F:\dash_app\dash_ibm_app\dataset\data_html\death_confirm'+str(i)+'.html')
    
import pandas as pd
#read the csv file as dataframe
csv_file=pd.read_csv(r'F:\dash_app\dash_ibm_app\dataset\morality_full_state_report_chatbot.csv')

for i in range(len(csv_file)):
    list=[csv_file.iloc[i,:]]
    df=pd.DataFrame(list)
    print(df)
    df.to_html(r'F:\dash_app\dash_ibm_app\dataset\data_html\fullreport'+str(i)+'.html')
    
data={"matching_results":1,"results":[
    {"enriched_text":
     {"categories":[{"label":"/health and fitness/disease/epidemic","score":0.754665}
                    ,{"label":"/health and fitness/disease/cold and flu","score":0.736139},
                    {"label":"/science/weather/meteorological disaster/hurricane","score":0.644663}],
      "concepts":[{"dbpedia_resource":"http://dbpedia.org/resource/Death","relevance":0.884667,"text":"Death"},
                  {"dbpedia_resource":"http://dbpedia.org/resource/Mortality_rate","relevance":0.7832,"text":"Mortality rate"},
                  {"dbpedia_resource":"http://dbpedia.org/resource/Demography","relevance":0.778862,"text":"Demography"},
                  {"dbpedia_resource":"http://dbpedia.org/resource/Mortality_displacement","relevance":0.748,"text":"Mortality displacement"}],
      "entities":[{"count":1,
                   "disambiguation":{"subtype":["Country"]},
                   "relevance":0.404372,
                   "sentiment":{"label":"neutral","score":0},
                   "text":"India","type":"Location"}],
      "sentiment":{"document":{"label":"negative","score":-0.620501}}},
     "extracted_metadata":{"file_type":"html","filename":"death_confirm79.html",
                           "sha1":"40f2c862b9315755f2ca636606b9c6329163abb9","title":"no title"},
     "html":"\n\n no title\n\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n
Mortality Rate (per 100)	Country_Region	Deaths	Confirmed
79	3.12	India	15301	490401
","id":"8fab4fd382c85a457ba5224dcf8305ae",
"result_metadata":{"confidence":0.08579440946271828,"score":7.618354},"text":"no title\n\nMortality Rate (per 100) Country_Region Deaths Confirmed\n\n79 3.12 India 15301 490401"}],
    "retrieval_details":{"document_retrieval_strategy":"untrained"},"session_token":"1_qp2GKMeMJdapp5z1_cauI1UUmI"}
 turn on n    
    
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:55:15 2020

@author: ninjaac
"""
data={"matching_results":1,
      "passages":[
          {"document_id":"d89b223847067067c78b4556c5404edb",
           "end_offset":83,"field":"text","passage_score":0,
           "passage_text":"Mortality Rate (per 100) Country_Region Deaths Confirmed 79 3.12 India 15301 490401",
           "start_offset":0}
          ],
      "results":[
          {"enriched_text":
                       {"categories":[
                           {"label":"/health and fitness/disease/epidemic",
                            "score":0.754907},
                           {"label":"/health and fitness/disease/cold and flu","score":0.732238},
                           {"label":"/science/weather/meteorological disaster/hurricane","score":0.644066}
                          ],
                        "concepts":[
                            {"dbpedia_resource":"http://dbpedia.org/resource/Death",
                             "relevance":0.884667,"text":"Death"},
                            {"dbpedia_resource":"http://dbpedia.org/resource/Mortality_rate",
                             "relevance":0.7832,"text":"Mortality rate"},
                            {"dbpedia_resource":"http://dbpedia.org/resource/Demography","relevance":0.778862,
                             "text":"Demography"},
                            {"dbpedia_resource":"http://dbpedia.org/resource/Mortality_displacement",
                             "relevance":0.748,"text":"Mortality displacement"}
                                        ],
                        "entities":[
                            {"count":1,
                             "disambiguation":{"subtype":["Country"]},
                             "relevance":0.33,"sentiment":{"label":"neutral","score":0},
                             "text":"India","type":"Location"}
                            ],
                        "sentiment":{"document":{"label":"neutral","score":0}}},
          "extracted_metadata":{"file_type":"pdf",
                                             "filename":"death_confirm79.pdf",
                                             "sha1":"f07558c1a9d14656b6f59c1c7f554ede5a241677"},
          "id":"d89b223847067067c78b4556c5404edb",
          "result_metadata":{"confidence":0.08551967715801696,"score":6.5645165},
          "text":"Mortality Rate (per 100) Country_Region Deaths Confirmed 79 3.12 India 15301 490401"}],
          "retrieval_details":{"document_retrieval_strategy":"untrained"},
          "session_token":"1_qp2GKMeMJdaLFGd2_cauI1UUmI"}
 
data["results"][0]['text']
    