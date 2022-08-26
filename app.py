import numpy as np
import os

from flask import (
    Flask,
    render_template,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# ---------------------------------------------------------
# Web site

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

@app.route("/acceptance_model" , methods=["POST"])
def acceptance_model():
    
    # <!-- Amount Requested, Loan Title, Debt-To-Income Ratio, State, Employment Length -->

    amount_requested = request.form["amount_requested"]
    if amount_requested == "":
        amount_requested = 14224.16
    amount_requested = float(amount_requested)
    
    loan_title = request.form["loan_title"]
    
    dti_ratio = request.form["dti_ratio"]
    if dti_ratio == "":
        dti_ratio = 88.77
    dti_ratio = float(dti_ratio)

    state = request.form["state"]

    emp_length = request.form["emp_length"]

    X = [[amount_requested, loan_title, dti_ratio, state, emp_length]]

    print(X)

    filename = './Models/loan_acceptance_scaler.sav'
    X_scaler = pickle.load(open(filename, 'rb'))
    
    X_scaled = X_scaler.transform(X)
    
    print(X_scaled)
    
    filename = './Models/loan_acceptance_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    print(loaded_model.predict(X_scaled))
        
    prediction = loaded_model.predict(X_scaled)
    
    prediction = prediction[0]
    
    if prediction == 0:
        prediction = "Declined"
    else:
        prediction = "Accepted"
    
    return render_template("index.html", prediction = prediction)
   
if __name__ == '__main__':
    app.run(debug=True)
