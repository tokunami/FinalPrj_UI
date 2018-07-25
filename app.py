import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, render_template, jsonify, redirect

# MongoDB if needed
# from flask_pymongo import PyMongo

# load other pythonscript
import getData

app = Flask(__name__)

# setup db
# db = os.path.join('db', 'marketData.sqlite')
# engine = create_engine(f"sqlite:///{db}")

# # reflect an existing database into a new model
# Base = automap_base()
# Base.prepare(engine, reflect=True)

# # Save references to each table
# Samples_Metadata = Base.classes.samples_metadata
# OTU = Base.classes.otu
# Samples = Base.classes.samples

# # Create our session (link) from Python to the DB
# session = Session(engine)

# use MongoDB if needed
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
# mongo = PyMongo(app)


@app.route('/')
def index():
    data = getData.dummy_func()
    # TODO load data from DB like these
    # mars = session.query(Samples).statement
    # mars = mongo.db.mars.find_one()
    return render_template('index.html', data=data)

@app.route('/data')
def getdata():
    # TODO call function which gets data from internal python file

    # mars = mongo.db.mars
    # mars_data = getData.dummy_func()
    # mars.update(
    #     {},
    #     mars_data,
    #     upsert=True
    # )
    return redirect('http://localhost:5000')


if __name__ == "__main__":
    app.run(debug=True)
