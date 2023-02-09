from turtle import shape
from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)

# Loading the model and passing the input to it for prediction


def model(arr):
    model = pickle.load(open("finalmodel.sav", "rb"))
    result = model.predict(np.array(arr).reshape(1, -1))
    return result


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Form page to take information from user
@app.route("/Form")
def Form():
    return render_template("Form.html")


# taking the information from the form and passing it to the model functio and return the result
@app.route("/result", methods=['POST'])
def result():
    Cholesterol = request.form.get('Cholesterol')
    Glucose = request.form.get('Glucose')
    HDL_col = request.form.get('HDL_col')
    Chol_HDL_Ratio = float(request.form.get('Chol_HDL_Ratio'))
    Age = request.form.get('Age')
    Gender = request.form.get('Gender')
    Height = request.form.get('Height')
    Weight = request.form.get('Weight')
    Bmi = float(request.form.get('BMI'))
    Systolic_bp = request.form.get('Systolic_bp')
    Diastolic_bp = request.form.get('Diastolic_bp')
    Waist = request.form.get('waist')
    Hip = request.form.get('hip')
    Waist_Hip_Ratio = float(request.form.get('Waist_Hip_Ratio'))
    arr = [Age, Gender, Height, Weight, Cholesterol, Glucose, HDL_col, Bmi,
           Chol_HDL_Ratio, Systolic_bp, Diastolic_bp, Waist, Hip, Waist_Hip_Ratio]
    result = model(arr)
    if result == 0:
        result = "No diabetes"
    else:
        result = "Diabetes"
    return render_template("result.html", Result=result)


if __name__ == '__main__':
    app.run(debug=True)
