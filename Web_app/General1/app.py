# -*- coding: utf-8 -*-
"""
Created on Sat Jan 08 16:09:33 2022

@author: Abdul Wajid
"""

# import libraries
from flask import Flask, request, render_template  # for get and post
import pandas as pd
import numpy as np


app = Flask(__name__)  # indicate where to start the app # return script name

# read data path
df = pd.read_csv("\Future_results1.csv")


@app.route("/")  # indicating root
def main():
    return render_template("./home.html ")  # render main page


@app.route("/predict", methods=["POST"])
def home():
    # save returened value
    data1 = request.form["month"]
    result_not_available = "Prediction not predicted yet"

    # select value
    if data1 == "2022-01":
        try:
            result = int(df.iloc[36, 3])
        except:
            result = result_not_available
    elif data1 == "2022-02":
        try:
            result = int(df.iloc[37, 3])
        except:
            result = result_not_available
    elif data1 == "2022-03":
        try:
            result = int(df.iloc[38, 3])
        except:
            result = result_not_available
    elif data1 == "2022-04":
        try:
            result = int(df.iloc[39, 3])
        except:
            result = result_not_available
    elif data1 == "2022-05":
        try:
            result = int(df.iloc[40, 3])
        except:
            result = result_not_available
    elif data1 == "2022-06":
        try:
            result = int(df.iloc[41, 3])
        except:
            result = result_not_available
    elif data1 == "2022-07":
        try:
            result = int(df.iloc[42, 3])
        except:
            result = result_not_available

    elif data1 == "2022-08":
        try:
            result = int(df.iloc[43, 3])
        except:
            result = result_not_available

    elif data1 == "2022-09":
        try:
            result = int(df.iloc[44, 3])
        except:
            result = result_not_available

    elif data1 == "2022-10":
        try:
            result = int(df.iloc[45, 3])
        except:
            result = result_not_available

    elif data1 == "2022-11":
        try:
            result = int(df.iloc[46, 3])
        except:
            result = result_not_available
    elif data1 == "2022-12":
        try:
            result = int(df.iloc[47, 3])
        except:
            result = result_not_available
    else:
        result = "Prediction not predicted yet"

    return render_template("prediction.html", data=result)  # render prediction page


if __name__ == "__main__":
    app.run(debug=True)  # no need to rerun just reload web page
