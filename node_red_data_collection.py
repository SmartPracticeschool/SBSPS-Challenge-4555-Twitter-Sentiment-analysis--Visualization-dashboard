import pandas as pd
import numpy as np

  
class sentiment_data():

    def get_sentiment_data():

        #read the files

        sentiment=pd.read_csv('sentiment.csv')
        sentiment.columns=['sentiment']
        emotion=pd.read_csv('emotion.csv')
        emotion.columns=['emotion']
        
        #future emotions and sentiment of people
        future_sentiment=pd.read_csv('sentiment_future.csv')
        future_sentiment.columns=['sentiment']
        
        #prepare the dataframe stuiable for pie chart
        sentiment_values=list(sentiment['sentiment'].value_counts())
        sentimet_names=['positive','negative','neutral']
        
        emotion_value=emotion['emotion'].value_counts()
        emotion_name=['fear','angery','joy','disgust','sadness']
        
        future_sentiment_value=list(future_sentiment['sentiment'].value_counts())
        future_sentimet_names=['positive','negative','neutral']
        
        #total values 
        sentiment_total=sentiment.shape[0]
        emotion_total=emotion.shape[0]
        future_sentiment_total=future_sentiment.shape[0]
        
        total=[sentiment_total,emotion_total,future_sentiment_total]
        
        return sentiment_values,sentimet_names,emotion_value,emotion_name,future_sentiment_value,future_sentimet_names,total
