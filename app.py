# Import Flask
from flask import Flask

# Create an app, being sure to pass __name__
app = Flask(__name__)

# 1. Define what to do when a user hits the index route
@app.route("/")
def home():
    return (
        f" Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )

# 2. Define what to do when a user hits the precipitation route
# Convert the query results to a Dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate lastest record date in the database
    session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    
    # Select the date and prcp "columns", filter the last twelve months of data and order by date
    last_twelve_mo = engine.execute("SELECT date, prcp FROM measurement WHERE date BETWEEN '2016-08-23' AND '2017-08-23' AND prcp NOT NULL ORDER BY date ASC")

    # Save the query results as a Pandas DataFrame
    twelve_mo_df = pd.DataFrame(last_twelve_mo.fetchall())

    # Rename DateFrame columns
    twelve_mo_df = twelve_mo_df.rename(columns = {0:'date', 1:'prcp'})
    # twelve_mo_df

    return jsonify (twelve_mo_df)

# 3. Define what to do when a user hits the stations route
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    stations = stations.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify (stations)

# 4. Define what to do when a user hits the tobs route
# Query for the dates and temperature observations from a year from the last data point.
# Return a JSON list of Temperature Observations (tobs) for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    station_tobs = session.query(Measurement.tobs).\
        filter(Measurement.station =='USC00519281').\
            filter(Measurement.date.between('2016-08-23', '2017-08-23')).all()
    stations_tobs = list(np.ravel(station_tobs))
    return jsonify (stations_tobs)

# 5. Define what to do when a user hits the <start> route
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
@app.route("/api/v1.0/<start>")
def start():
    # create function variable for min, max and avg temps
    tobs = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    # Query the min, max & avg tobs for given start date
    start_tob = session.query(*tobs).filter(Measurement.date >= start).all()
    start_tob = list(np.ravel(start_tob))
    return jsonify (start_tob)

# 6. Define what to do when a user hits the start_end route
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
@app.route("/api/v1.0/<start>/<end>")
def start_end():
    # Query the min, max & avg tobs for given start & end dates
    result = session.query(*tobs).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    start_end_tobs = list(np.ravel(result))
    return jsonify (start_end_tobs)

if __name__ == '__main__':
    app.run()