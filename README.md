# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     Covid19 - A Live 
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  user interactive Sentiment and Emotion Dashboard
___
### Table of Content:
-	[About the project](#about-the-project) 
-	[Getting started](#getting-started)
-	[Dashboard Fundamentals](#dashboard-fundamentals)
-	[Resources](#resources) 
-	[Team members](#team-members)
# About the project:
<b>It presents  live streaming, fully user interactive, all-in-one dashboard with live sentiment and emotions of people</b> across the world about the COVID19 lockdown. 
-	This app will give you the covid19 death and confirmed cases information for whole world as well as for each country. You can get the daily update on covid19 through the dashboard.
-	The main parts of the dashboard is <b><i>“Sentiment of people about covid19, Emotion of people about covid19 and the main Sentiment of people If the lockdown is extended”.</i></b> 
They are updated every 5 seconds.
-	<b>World map</b> is plotted with all the countries in the world and updated every day. When hover on one country ,this  will generate two graph showing death and confirmed cases corresponding to the country from may to now day-wise. This graph is fully user interactive, when user hover on it the graph keep updating corresponding to every point they hovering.
-	<b><i>Mortality rate</i></b> – mortality rate is nothing but the death rate. Through the mortality rate we can decide the covid19 condition in the country.
-	<b><i>Al Based CovidBot</i></b>- dashboard is available with the CovidBot through that we can contact with our AI chatbot and make communication about  the general information, treatment and medical related queries, origin, present condition, sentiment and emotion analytics graph, death and confirmed cases county-wise and more.
- You can <b><i>download the images</i></b> from the camera icon on the side of the images.


# Getting started:
-	clone the repository
- For chatbot creation [follow the steps here](https://github.com/pavi-ninjaac/Covid19Bot)
- For live sentiment stream [follow the steps here](https://github.com/pavi-ninjaac/Sentiment_analyse_node-red) 
- run main.py file from your cmd like “python main.py”
-	view the dash app on localhost:8050

# Dashboard Fundamental:
Here is the live, user interactive visualization dashboard to visualize the sentiment and emotion about Covid19 lockdown. center part first visualize the Sentiment of people through the pie chart and hover on the pie chat will give you the general information and number of tweets under the catogary. This is updated every 5 seconds.<br/>

![Screenshot (179)](https://user-images.githubusercontent.com/51699297/87278555-65fe6a00-c502-11ea-8288-629ae7748022.png)

- Secondly the main part of the project is “sentiment if the lockdown is extended “ will also give you the pie chart with future predicted sentiment about the lockdown with hover information.<br/>

![Screenshot (174)](https://user-images.githubusercontent.com/51699297/87278474-2b94cd00-c502-11ea-82f8-b8ad32b84548.png)

- Third “Emotion of the people during covid19 “ visualizes the bar chat for 5 emotions and updated every 5 seconds.<br/>

![Screenshot (177)](https://user-images.githubusercontent.com/51699297/87278553-63037980-c502-11ea-907c-6c6dc18a845a.png)

- <b><i>At the right and lift side of the dashboard  you can see the total death, confirmed and active cases and a list of death an confirmed cases country-wise. This will update you more about covid19 and ordered in decending so the country which has the highest count will appear first.</i></b><br/><br/><br/>

- World map if you hover on it the right side two graphs are updated based on the county you hovering. Fully user interactive.<br/>

![Screenshot (175)](https://user-images.githubusercontent.com/51699297/87278491-364f6200-c502-11ea-8678-badd74e51f07.png)

- Mortality map visualizes the highest 25 counties which has the high mortality rate value and when you hover on it you can see more information about the mortality and the coutry.<br/>

![Screenshot (176)](https://user-images.githubusercontent.com/51699297/87278522-46674180-c502-11ea-8ec7-5e65082c18ec.png)

- CovidBot – can answer users based on the AI technology<br/>

![Screenshot (183)](https://user-images.githubusercontent.com/51699297/87293388-debfef00-c51f-11ea-83a7-d810dee55a4a.png)

- You can download any image from the camera icon on the image, you can see that when you hover on the imgaes.

![Screenshot (188)](https://user-images.githubusercontent.com/51699297/87303121-3d8d6480-c530-11ea-8ffe-6e748a6c3430.png)

# Resources:
-	Dash – powerful tool for live data visualization with plotly python
-	Tone analyser –  IBM tone analyser used for getting the emotions of the people base on tweets
-	NLU – A methodology that used to get the sentiment of the people
-	Twitter Node in node-red – Tweets collection tool using the twitter API
-	Cloudant – A NoSQL database on IBM
-	IBM Watson – used to create the CovidBot without coding 
-	Dicovery – IBM discovery service used to give a AI power to my covidbot
-	Node-red – to integrate all those things
-	IBM API – model will be deployed on IBM

# Report Links:
- Final Report link: 
- Video Demonstration Link :
- ppt Link :

# Team members:
-	[Pavithra Devi](https://github.com/pavi-ninjaac)
-	[Pooja  Laxshmi](https://github.com/PoojaChidambaram)
-	[Ponmalar](https://github.com/Agnes-source)
