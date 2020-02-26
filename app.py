# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy import desc
from sqlalchemy import distinct
from sqlalchemy import func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd

import numpy as np
import pandas as pd
import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Import Flask
from flask import Flask, jsonify

# Create an app, being sure to pass __name__
app = Flask(__name__)

# 1. Define what to do when a user hits the index route
@app.route("/")
def home():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f" Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

# 2. Define what to do when a user hits the precipitation route
# Convert the query results to a Dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate lastest record date in the database
    session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    # Select the date and prcp "columns", filter the last twelve months of data and order by date
    twelve_mo_prcp = engine.execute("SELECT date, prcp FROM measurement WHERE date BETWEEN '2016-08-23' AND '2017-08-23' AND prcp NOT NULL ORDER BY date ASC")
    # Save the query results as a DataFrame
    twelve_mo_prcp_df = pd.DataFrame(twelve_mo_prcp, columns= ['date','prcp'])
    # twelve_mo_prcp_df
    return twelve_mo_prcp_df.to_json(orient='records')
    # return jsonify (twelve_mo_prcp_df)

# 3. Define what to do when a user hits the stations route
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Station.station).all()
    stations = list(np.ravel(stations))
    return jsonify (stations)

# 4. Define what to do when a user hits the tobs route
# Query for the dates and temperature observations from a year from the last data point.
# Return a JSON list of Temperature Observations (tobs) for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    twelve_mo_tobs = engine.execute("SELECT date, tobs FROM measurement WHERE date BETWEEN '2016-08-23' AND '2017-08-23' ORDER BY date ASC")
    twelve_mo_tobs_df = pd.DataFrame(twelve_mo_tobs, columns= ['date','tobs'])
    return twelve_mo_tobs_df.to_json(orient='records')
    # return jsonify (twelve_mo_tobs_df)

# 5. Define what to do when a user hits the <start> route
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
@app.route("/api/v1.0/<start>")
def start(start):
    # create function variable for min, max and avg temps
    tobs = [func.min(Measurement.tobs), func.max(Measurement.tobs),func.avg(Measurement.tobs)]
    # Query the min, max & avg tobs for given start date
    start_tob = session.query(*tobs).filter(Measurement.date >= start).all()
    start_tob = list(np.ravel(start_tob))
    return jsonify (start_tob)

# 6. Define what to do when a user hits the start_end route
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
#    # Query the min, max & avg tobs for given start & end dates
    tobs = [func.min(Measurement.tobs), func.max(Measurement.tobs),func.avg(Measurement.tobs)]
    start_end_tobs = session.query(*tobs).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    start_end_tobs = list(np.ravel(start_end_tobs))
    # start_end_tobs = list(np.ravel(result))
    return jsonify (start_end_tobs)
#     lowest_temp = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
#     lowest_temp = list(np.ravel(lowest_temp))
#     return jsonify (lowest_temp)

# highest_temp = session.query(func.max(Measurement.tobs)).\
#  filter(Measurement.station =='USC00519281').\
#  order_by(Measurement.tobs.asc()).scalar()
# avg_temp = session.query(func.avg(Measurement.tobs)).filter(Measurement.station =='USC00519281').scalar()

# print(f"[({lowest_temp}, {highest_temp}, {avg_temp})]")

if __name__ == "__main__":
    app.run(debug=True)