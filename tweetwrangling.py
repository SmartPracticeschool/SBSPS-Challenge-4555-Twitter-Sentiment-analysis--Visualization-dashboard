# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:51:54 2020

@author: ninjaac
"""

import pandas as pd

import numpy as np


from datetime import date, timedelta


class tweets_analyse():
    def get_data():
        today = date.today()
        yesterday = today - timedelta(days=1)

        d1 = yesterday.strftime("%m-%d-%Y")

        
        fileurl = r'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + d1 + '.csv'
        df = pd.read_csv(fileurl)

        df.head()
        df.columns
        """Index(['FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Last_Update',
       'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active',
       'Combined_Key', 'Incidence_Rate', 'Case-Fatality_Ratio'],
      dtype='object')"""


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
        
        morality_df.to_csv(r'F:\dash_app\dash_ibm_app\dataset\morality_full_state_report_chatbot.csv')
        
        morality_sorted =morality_df.sort_values(by='Mortality Rate (per 100)',ascending=False)    
        top_25_cities=morality_sorted.iloc[0:25,:]
        
                    
        # total confirmed along with contries
        total_confirmed = df_consolidated['Confirmed'].sum()
        confirm_country=df_consolidated[['Confirmed','Country_Region']].copy()
        sorted_confirmed =confirm_country.sort_values(by='Confirmed',ascending=False)

    
        # total deaths along with contries
        total_deaths = df_consolidated['Deaths'].sum()
        death_country=df_consolidated[['Deaths','Country_Region']].copy()
        sorted_death=death_country.sort_values(by='Deaths',ascending=False)
        
        
        
        total_recovered = df_consolidated['Recovered'].sum()
        recovery_country=df_consolidated[['Recovered','Country_Region']].copy()
        sorted_recovered =recovery_country.sort_values(by='Recovered',ascending=False)


        return total_confirmed,sorted_confirmed,total_deaths,sorted_death,total_recovered,sorted_recovered,top_25_cities
    
    
    def time_series_creation():
        
        df_confirmed_ts = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        df_deaths_ts =    pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        df_recovered_ts = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
   
        
        df_lat_long_confirm=df_confirmed_ts[['Country/Region','Lat','Long']]


        # remove the columns representing the Latitude and longitude of the locations
        df_confirmed_ts.drop(columns=['Lat','Long'],inplace=True)
        df_deaths_ts.drop(columns=['Lat','Long'],inplace=True)
        df_recovered_ts.drop(columns=['Lat','Long'],inplace=True)
        
        # consolidate the data as per the country

        df_confirmed_con = df_confirmed_ts.groupby(by='Country/Region').sum()
        df_recovered_con = df_recovered_ts.groupby(by='Country/Region').sum()
        df_death_con = df_deaths_ts.groupby(by='Country/Region').sum()
        

        # transpose the dataframe 
        df_confirmed_con = df_confirmed_con.transpose()
        df_recovered_con = df_recovered_con.transpose()
        df_death_con = df_death_con.transpose()


        # add date column to the data frame
        df_confirmed_con['date'] = df_confirmed_con.index
        df_death_con['date'] = df_death_con.index
        df_recovered_con['date'] = df_recovered_con.index

        # convert the data into long form in order to merge the data
        df_confirmed_long = df_confirmed_con.melt(id_vars=['date'],value_name='Confirmed')
        df_death_long = df_death_con.melt(id_vars=['date'],value_name='Death')
        df_recovered_long = df_recovered_con.melt(id_vars=['date'],value_name='Recovered') 

        # merge the data
        full_table = df_confirmed_long.merge(right=df_death_long, how='left',
                                     on=['Country/Region', 'date'])

        full_table = full_table.merge(right=df_recovered_long, how='left',
                                     on=['Country/Region', 'date'])   
        
        df_lat_long_confirm_f=df_lat_long_confirm.groupby('Country/Region',as_index=False).max()
        df_lat_long_confirm_f['Country/Region'].value_counts()

        full_table_f=full_table.merge(right=df_lat_long_confirm_f,how='outer',
                                on=['Country/Region'])
        
        
        return full_table_f
