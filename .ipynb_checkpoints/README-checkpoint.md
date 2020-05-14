# SQL_Alchemy

"SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL."
https://www.sqlalchemy.org/

## Climate Analysis and Exploration

Python and SQLAlchemy used for a climate analysis of precipitation and station activity in Honolulu, Hawaii within a 12-month timeframe.

Queries designed in a Jupyter Lab notebook sourced in a .sqlite file.

The following languages used to organize and visualize data: SQLAlchemy ORM queries, Pandas, and Matplotlib.

## Precipitation Analysis

1. Structured and sorted a pandas dataFrame to provide data by date and precipitation levels.  
2. Built a matplotlib graph to display daily precipitation

![](twelve_mo_prcp.png)

## Station Analysis
1. Queries designed to calculate the total number of stations, the most active stations & stations with the highest number of temperature observation data (tobs).
2. Designed a query to retrieve the last 12 months of temperature observation data (tobs).
3. Results plotted  as a histogram.

![](tobs_histogram.png)
