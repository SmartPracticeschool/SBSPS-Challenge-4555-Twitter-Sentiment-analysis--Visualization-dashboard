# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:20:24 2020

@author: ninjaac
"""

from cloudant import cloudant
from cloudant.client import Cloudant
import pandas as pd
import json
from cloudant.result import Result, ResultByKey  
Url='https://1aa35899-513b-4f79-b810-d0aa854e70b6-bluemix:e40e9b009bb1d8621dc1c8467186e53d8ef8f4d5e30e3950efe3084b9c77348b@1aa35899-513b-4f79-b810-d0aa854e70b6-bluemix.cloudantnosqldb.appdomain.cloud'
"""
    client = Cloudant(USERNAME, PASSWORD, url=your url)
        
    client = Cloudant('995d72fd-116c-482b-9b38-8d60481f9a86-bluemix', 
                      '2a7c7a6833e3aaa17ee8644a1bfbec515a4403de17136678610e08045e5bc27f',
              url=Url
             )
 

"""
client= Cloudant('1aa35899-513b-4f79-b810-d0aa854e70b6-bluemix', 
                  'e40e9b009bb1d8621dc1c8467186e53d8ef8f4d5e30e3950efe3084b9c77348b',
                  url=Url,connect=True,auto_renew=True,
                  ) 
   
session = client.session()
print('Username: {0}'.format(session['userCtx']['name']))
print('Databases: {0}'.format(client.all_dbs()))
        
#open the database
sentiment_db = client['sentiment']
result=Result(sentiment_db.all_docs,include_docs=True)
r=result[0]
for i in sentiment_db:
    print( i)
print(sentiment_db)
#emosion_db=client['emotion']
#tweet_db=client['tweets']
for i in sentiment_db:
    print(i)    
#retrive all the documents
res=sentiment_db.all_docs(include_docs=True)
file=open(r'F:\dash_app\dash_ibm_app\dataset\sentimetn.json','w')
for ans in res['rows']:
    print(ans['doc'])
    json.dump(ans["doc"],file,indent=6)

json=pd.read_json(r'F:\dash_app\dash_ibm_app\dataset\sentimetn.json')
sentiment=[]
"""
      for data in sentiment_db:
            sentiment.append(data['SENTIMENT'])
        print('dmwjcm')
"""
        #sentiment_df=pd.DataFrame(data=sentiment,columns='sentiment')
          

        