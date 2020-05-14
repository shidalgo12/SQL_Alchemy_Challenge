# SQL_Alchemy

Queried climate data of Honolulu, Hawaii to observe 12-months of precipitation and station activitiy throughout the island.

## Climate Analysis and Exploration

Python and SQLAlchemy used for a climate analysis and data exploration in a Jupyter Lab notebook and .sqlite file.

The following languages used to organize and visualize data: SQLAlchemy ORM queries, Pandas, and Matplotlib.


## Precipitation Analysis

1. Structured and sorted a pandas dataFrame to solely provide data by date and precipitation levels.  
2. Built a matplotlib to display daily precipitation

![](twelve_mo_prcp.png)

## Station Analysis


Design a query to calculate the total number of stations.


Design a query to find the most active stations.


List the stations and observation counts in descending order.


Which station has the highest number of observations?


Hint: You may need to use functions such as func.min, func.max, func.avg, and func.count in your queries.




Design a query to retrieve the last 12 months of temperature observation data (tobs).


Filter by the station with the highest number of observations.


Plot the results as a histogram with bins=12.







Step 2 - Climate App
Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

Use FLASK to create your routes.


Routes


/


Home page.


List all routes that are available.




/api/v1.0/precipitation


Convert the query results to a Dictionary using date as the key and prcp as the value.


Return the JSON representation of your dictionary.




/api/v1.0/stations

Return a JSON list of stations from the dataset.



/api/v1.0/tobs

query for the dates and temperature observations from a year from the last data point.
Return a JSON list of Temperature Observations (tobs) for the previous year.



/api/v1.0/<start> and /api/v1.0/<start>/<end>


Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.


When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.


When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.