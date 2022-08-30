import pickle
# import numpy as np
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
##################################################
# Model 1
##################################################
@app.route("/acceptance_model" , methods=["POST"])
def acceptance_model():
    
    # <!-- Amount Requested, Loan Title, Debt-To-Income Ratio, State, Employment Length -->

    amount_requested = request.form["amount_requested"]
    if amount_requested == "":
        amount_requested = 14224.16
    amount_requested = float(amount_requested)
    
    loan_title = request.form["loan_title"]
    
    Loan_Title_AUTO = Loan_Title_BUSINESS = Loan_Title_CC = Loan_Title_DEBT_CONSOLIDATION =\
    Loan_Title_EDUCATION = Loan_Title_HOME = Loan_Title_IMPROVEMENT = Loan_Title_MAJOR_PURCHASE =\
    Loan_Title_MEDICAL = Loan_Title_No_Response = Loan_Title_Other = Loan_Title_PAYOFF =\
    Loan_Title_WEDDING = Loan_Title_renewable_energy = Loan_Title_vacation = 0
    def LT(lt):
        if lt == 'DEBT_CONSOLIDATION': Loan_Title_DEBT_CONSOLIDATION = 1
        if lt ==  'CC'				 : Loan_Title_CC = 1
        if lt ==  'IMPROVEMENT'		 : Loan_Title_IMPROVEMENT = 1
        if lt ==  'No Response'		 : Loan_Title_No_Response = 1
        if lt ==  'Other'			 : Loan_Title_Other = 1
        if lt ==  'MAJOR_PURCHASE'	 : Loan_Title_MAJOR_PURCHASE = 1
        if lt ==  'HOME'			 : Loan_Title_HOME = 1
        if lt ==  'MEDICAL'			 : Loan_Title_MEDICAL = 1
        if lt ==  'BUSINESS'		 : Loan_Title_BUSINESS = 1
        if lt ==  'AUTO'			 : Loan_Title_AUTO = 1
        if lt ==  'vacation'		 : Loan_Title_vacation = 1
    
    LT(loan_title)

    dti_ratio = request.form["dti_ratio"]
    if dti_ratio == "":
        dti_ratio = 88.77
    dti_ratio = float(dti_ratio)

    state = request.form["state"]

    State_AK = State_AL = State_AR = State_AZ = State_CA = State_CO = State_CT = \
    State_DC = State_DE = State_FL = State_GA = State_HI = State_IA = \
    State_ID = State_IL = State_IN = State_KS = State_KY = State_LA = \
    State_MA = State_MD = State_ME = State_MI = State_MN = State_MO = \
    State_MS = State_MT = State_NC = State_ND = State_NE = State_NH = \
    State_NJ = State_NM = State_NV = State_NY = State_OH = State_OK = \
    State_OR = State_PA = State_RI = State_SC = State_SD = State_TN = \
    State_TX = State_UT = State_VA = State_VT = State_WA = State_WI = \
    State_WV = State_WY = 0

    def ST(st):
        if st == 'State_AK' : State_AK = 1
        if st == 'State_AL' : State_AL = 1
        if st == 'State_AR' : State_AR = 1
        if st == 'State_AZ' : State_AZ = 1
        if st == 'State_CA' : State_CA = 1
        if st == 'State_CO' : State_CO = 1
        if st == 'State_CT'	: State_CT = 1
        if st == 'State_DC' : State_DC = 1
        if st == 'State_DE' : State_DE = 1
        if st == 'State_FL' : State_FL = 1
        if st == 'State_GA' : State_GA = 1
        if st == 'State_HI' : State_HI = 1
        if st == 'State_IA' : State_IA = 1
        if st == 'State_ID' : State_ID = 1
        if st == 'State_IL' : State_IL = 1
        if st == 'State_IN' : State_IN = 1
        if st == 'State_KS' : State_KS = 1
        if st == 'State_KY' : State_KY = 1
        if st == 'State_LA' : State_LA = 1
        if st == 'State_MA' : State_MA = 1
        if st == 'State_MD' : State_MD = 1
        if st == 'State_ME' : State_ME = 1
        if st == 'State_MI' : State_MI = 1
        if st == 'State_MN' : State_MN = 1
        if st == 'State_MO' : State_MO = 1
        if st == 'State_MS' : State_MS = 1
        if st == 'State_MT' : State_MT = 1
        if st == 'State_NC' : State_NC = 1
        if st == 'State_ND' : State_ND = 1
        if st == 'State_NE' : State_NE = 1
        if st == 'State_NH' : State_NH = 1
        if st == 'State_NJ' : State_NJ = 1
        if st == 'State_NM' : State_NM = 1
        if st == 'State_NV' : State_NV = 1
        if st == 'State_NY' : State_NY = 1
        if st == 'State_OH' : State_OH = 1
        if st == 'State_OK' : State_OK = 1
        if st == 'State_OR' : State_OR = 1
        if st == 'State_PA' : State_PA = 1
        if st == 'State_RI' : State_RI = 1
        if st == 'State_SC' : State_SC = 1
        if st == 'State_SD' : State_SD = 1
        if st == 'State_TN' : State_TN = 1
        if st == 'State_TX' : State_TX = 1
        if st == 'State_UT' : State_UT = 1
        if st == 'State_VA' : State_VA = 1
        if st == 'State_VT' : State_VT = 1
        if st == 'State_WA' : State_WA = 1
        if st == 'State_WI' : State_WI = 1
        if st == 'State_WV' : State_WV = 1
        if st == 'State_WY' : State_WY = 1

    ST(state)

    emp_length = request.form["emp_length"]

    X = [[amount_requested, dti_ratio, emp_length,
        Loan_Title_AUTO, Loan_Title_BUSINESS, Loan_Title_CC, Loan_Title_DEBT_CONSOLIDATION,
        Loan_Title_EDUCATION, Loan_Title_HOME, Loan_Title_IMPROVEMENT, Loan_Title_MAJOR_PURCHASE,
        Loan_Title_MEDICAL, Loan_Title_No_Response, Loan_Title_Other, Loan_Title_PAYOFF,
        Loan_Title_WEDDING, 0,
        
        Loan_Title_renewable_energy, Loan_Title_vacation,
        State_AK, State_AL, State_AR, State_AZ, State_CA, State_CO, State_CT,
        State_DC, State_DE, State_FL, State_GA, State_HI, State_IA,
        State_ID, State_IL, State_IN, State_KS, State_KY, State_LA,
        State_MA, State_MD, State_ME, State_MI, State_MN, State_MO,
        State_MS, State_MT, State_NC, State_ND, State_NE, State_NH,
        State_NJ, State_NM, State_NV, State_NY, State_OH, State_OK,
        State_OR, State_PA, State_RI, State_SC, State_SD, State_TN,
        State_TX, State_UT, State_VA, State_VT, State_WA, State_WI,
        State_WV, State_WY]]

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


##################################################
# Model 2
##################################################
@app.route("/time_model" , methods=["POST"])
def time_model():
    
    # <!-- "recoveries","total_rec_late_fee","total_rec_prncp","delinq_2yrs","fico_range_high","loan_status","total_pymnt"-->

    recoveries = request.form["recoveries"] #text
    if recoveries == "":
        recoveries = 154.89
    recoveries = float(recoveries)
        
    total_rec_late_fee = request.form["total_rec_late_fee"] #text
    if total_rec_late_fee == "":
        total_rec_late_fee = 1.48
    total_rec_late_fee = float(total_rec_late_fee)
    
    total_rec_prncp = request.form["total_rec_prncp"] #text
    if total_rec_prncp == "":
        total_rec_prncp = 9853.52
    total_rec_prncp = float(total_rec_prncp)

    delinq_2yrs = request.form["delinq_2yrs"] # text or dropdown 0-16, 18, 19

    fico_range_high = request.form["fico_range_high"] #text
    if fico_range_high == "":
        fico_range_high = 701.15
    fico_range_high = float(fico_range_high) 

    loan_status = request.form["loan_status"] #dropdown --> Fully Paid vs Late

    total_pymnt = request.form["total_pymnt"] #text
    if total_pymnt == "":
        total_pymnt = 12517.59
    total_pymnt = float(total_pymnt)

    X = [[recoveries, total_rec_late_fee, total_rec_prncp, delinq_2yrs, fico_range_high, loan_status, total_pymnt]]

    print(X)

    filename = './Models/loan_status_scaler.sav'
    X_scaler = pickle.load(open(filename, 'rb'))
    
    X_scaled = X_scaler.transform(X)
    
    print(X_scaled)
    
    filename = './Models/new_status_predictor.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    print(loaded_model.predict(X_scaled))
        
    prediction = loaded_model.predict(X_scaled)
    
    prediction = prediction[0]
    
    if prediction == 0:
        prediction = "Late"
    else:
        prediction = "Fully Paid"
    
    return render_template("index.html", prediction = prediction)
   
if __name__ == '__main__':
    app.run(debug=True)

