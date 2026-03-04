from flask import Flask,render_template,request
import joblib
import numpy as np


model = joblib.load("model.pkl")


app=Flask(__name__)

'''@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"'''


'''@app.route("/about")
def about():
    return render_template("index.html")'''

@app.route("/")
def myform():
    return render_template("myform.html")

@app.route("/predict",methods=["POST"])
def predict():
    area = float(request.form["area"])
    bedroom = float(request.form["bedroom"])
    age= float(request.form["age"])

    feature = np.array([[area,bedroom,age]])
    prediction = model.predict(feature)
    return render_template("myform.html",Prediction_text=f"House price is {prediction[0]}")

if __name__ == "__main__":
    app.run(debug=True)
