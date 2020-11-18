#Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
#Set up database engine
engine = create_engine("sqlite:///hawaii.sqlite")
#Reflect the database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)
#Create references to each table 
Measurement = Base.classes.measurement
Station = Base.classes.station
#Create a session link from Python to database
session = Session(engine)

#Define our flask app
app = Flask(__name__)
#Define the welcome root
@app.route("/")
#Define the welcome function
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
#Define the precipitation route
@app.route("/api/v1.0/precipitation")
#Define the precipitation function
def precipitation():
    #Add code to look at the previous year starting 8/23/2017
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    #Add code to capture the precipitation data from previous year identified above
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    #Create a dictionary to store all the returned data
    precip = {date: prcp for date, prcp in precipitation}
    #jsonify the data
    return jsonify(precip)
#Define the stations route
@app.route("/api/v1.0/stations")
#Define the stations function
def stations():
    #Add a query to get all the names of stations in the DB
    #variable = start.query(Table.column).printall()
    results = session.query(Station.station).all()
    #unravel results into a one-dimensional array (flat-file)
    stations = list(np.ravel(results))
    #jsonify the data - special code added to format list
    return jsonify(stations=stations)
#define the temperature observations route
@app.route("/api/v1.0/tobs")
#Define the monthly temp function
def temp_monthly():
    #Add code to look at the previous year starting 8/23/2017
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    #query primary station for all temp obs from previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
            filter(Measurement.date >= prev_year).all()
    #Unravel results into a one-dimensional array (Flat-file)
    temps = list(np.ravel(results))
    #jsonify the data
    return jsonify(temps=temps)
#define the route for starting and ending temperature analysis
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
#define the stats function
#add parameters for start time and end time
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)