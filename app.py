import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template
from sqlalchemy import inspect 
 
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Database Setup
#################################################
lending_tree_engine = create_engine("sqlite:///data.sqlite")

#status_engine = create_engine("sqlite:///status.db")
# reflect an existing database into a new model
Lending_Tree_Base = automap_base()

# reflect the tables
Lending_Tree_Base.prepare(lending_tree_engine, reflect=True)

# Save reference to the table
# print(Lending_Tree_Base.classes.keys())

lending_tree_data = Lending_Tree_Base.classes

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def home():
    return render_template("index.html")

# LIST ALL AVAILABLE ROUTES
# @app.route("/api")
# @app.route("/api/")
# def welcome():
#     """List all available api routes."""
#     return (
#         f"<h2>Available Routes:<h2/><hr>"
        
#         f"<h4>1: Return first 1,000 of all kaggle results:</h4><a href='/api/v1.0/kaggle'>/api/v1.0/kaggle</a><br/><hr><br>"
#         f"<h4>2: Returns all unique makes in kaggle:</h4><a href='/api/v1.0/kaggle/makes'>/api/v1.0/kaggle/makes</a><br/><hr><br>"
#         f"<h4>3: Returns summary data for a single make in Kaggle Data:</h4> /api/v1.0/kaggle/makes/&lt;brand&gt;<br/><br>\
#             Brand must exist in #2<hr>"


#         f"<h4>4: Returns all results from Cargurus Scraped Data:<h4><a href='/api/v1.0/scraped'>/api/v1.0/scraped</a><br/><hr><br>"
#         f"<h4>5: Returns all unique makes in Cargurus Scraped Data:</h4><a href='/api/v1.0/scraped/makes'>/api/v1.0/scraped/makes</a><br/><hr><br>"
#         f"<h4>6: Returns summary data for a single make in Cargurus Scraped Data:</h4> /api/v1.0/scraped/makes/&lt;brand&gt;<br/><br>\
#             Brand must exist in #5<hr>"
#         f"<h4>7: Returns gouge score for all dealers:<h4><a href='/api/v1.0/scraped/gouge'>/api/v1.0/scraped/gouge</a><br/><hr><br>"
#         f"<h4>8: Returns summary data for a single make in Cargurus Scraped Data:</h4> /api/v1.0/scraped/msrp/&lt;make&gt;<br/><br>\
#             Brand must exist in #5<hr>"
#     )

@app.route("/lending_tree_data")
def data():
    session = Session(lending_tree_engine)
    
     # Perform a query to retrieve the data and precipitation scores
    lending_tree_list = lending_tree_engine.execute("SELECT * FROM sales").fetchall()
   
    inspector = inspect(lending_tree_engine)
    columns = inspector.get_columns('sales')
    column_names=[]
    for c in columns:
        column_names.append(c['name'])
    
   # Create a list of dictionaries to JSONify later for easy plotting
    output_list=[]
    # for the first 10 entries in kaggle_list coming from cis_2018.sqlite database...
    for l in lending_tree_list[0:1000]:
        temp_dict={}
    #this is where we assign column rows to their corresponding column names
        for c in range(0,len(column_names)):
            temp_dict[column_names[c]]=l[c]
    #append temp_dict to output_list
        output_list.append(temp_dict)
    output_list

    session.close()

    return (
        jsonify (output_list)
    )  
   
if __name__ == '__main__':
    app.run(debug=True)
