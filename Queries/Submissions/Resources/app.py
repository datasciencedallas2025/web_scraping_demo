import numpy as np
import pandas as pd
from sqlalchemy import create_engine, engine
from flask import Flask, jsonify
import json



#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    return (f"Welcome to the Hawaii Weather Station API!</br>"
            f"Available Routes:</br>"
            f"<a href ='/api/v1.0/stations'>stations</a></br>"
            f"<a href ='/api/v1.0/precipitation'>precipitation</a></br>"
            f"<a href ='/api/v1.0/tobs'>tobs</a></br>"
            f"<a href ='/api/v1.0/2016-09-17'>start----Date must be in yyyy-mm-dd format</a></br>"
            f"<a href ='/api/v1.0/2016-09-17/2016-10-07'>start/end-----Date must be in yyyy-mm-dd format</a></br>"
    )

@app.route("/api/v1.0/stations")
def stations():
    conn = engine.connect()

    query = "SELECT * from station"
    df = pd.read_sql(query, con=conn)
    conn.close()

    data = df.to_json(orient="records") # creates JSON string
    data = json.loads(data) # turns the string back into list of dicts

    return jsonify({"ok": True, "data": data})

@app.route("/api/v1.0/precipitation")
def precipitation():
    conn = engine.connect()

    query = f"""
                SELECT
                    date,
                    avg (prcp) as average_prcp
                FROM
                    measurement
                GROUP BY
                    date
                ORDER BY
                    date asc;
            """
    df = pd.read_sql(query, con=conn)
    conn.close()

    data = df.to_json(orient="records") # creates JSON string
    data = json.loads(data) # turns the string back into list of dicts

    return jsonify({"ok": True, "data": data})

@app.route("/api/v1.0/tobs")
def tobs():
    conn = engine.connect()

    query = f"""
            SELECT
                station,
                date,
                tobs as temperature
            FROM
                measurement m
            WHERE
                m.station='USC00519281'
                and date >= '2016-08-23'
            ORDER BY
                date asc;
             
        """

    df = pd.read_sql(query, con=conn)
    conn.close()

    data = df.to_json(orient="records") # creates JSON string
    data = json.loads(data) # turns the string back into list of dicts

    return jsonify({"ok": True, "data": data})

@app.route("/api/v1.0/<start>") # Date must be in yyyy-mm-dd format
def start(start):
    conn = engine.connect()

    query = f"""
            SELECT
                date,
                min(tobs) as min_temp,
                avg(tobs) as avg_temp,
                max(tobs) as max_temp
            FROM
                measurement m
            WHERE
                date = '{start}'
             
        """

    df = pd.read_sql(query, con=conn)
    conn.close()

    data = df.to_json(orient="records") # creates JSON string
    data = json.loads(data) # turns the string back into list of dicts

    return jsonify({"ok": True, "data": data})

@app.route("/api/v1.0/<start>/<end>") # Date must be in yyyy-mm-dd format
def dateRange(start, end):
    conn = engine.connect()

    query = f"""
            SELECT
                min(date) as startDate,
                max(date) as endDate,
                min(tobs) as min_temp,
                avg(tobs) as avg_temp,
                max(tobs) as max_temp
            FROM
                measurement m
            WHERE
                date >= '{start}'
                and date <= '{end}'
        """

    df = pd.read_sql(query, con=conn)
    conn.close()

    data = df.to_json(orient="records") # creates JSON string
    data = json.loads(data) # turns the string back into list of dicts

    return jsonify({"ok": True, "data": data})

if __name__ == '__main__':
    app.run(debug=True)
