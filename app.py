from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib
import os

app = Flask(__name__)
model = joblib.load("student_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form")
def form():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    required_fields = ["hours_studied", "attendance", "previous_score"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is missing"}), 400

    try:
        features = np.array([[ 
            float(data["hours_studied"]),
            float(data["attendance"]),
            float(data["previous_score"])
        ]])

        prediction = model.predict(features)[0]
        return jsonify({"result": int(prediction)})

    except:
        return jsonify({"error": "Invalid input"}), 400


@app.route("/predict-form", methods=["POST"])
def predict_form():
    try:
        hours = float(request.form["hours_studied"])
        attendance = float(request.form["attendance"])
        score = float(request.form["previous_score"])

        features = np.array([[hours, attendance, score]])
        prediction = model.predict(features)[0]

        result = "Pass" if prediction == 1 else "Fail"
        return render_template("index.html", result=result)

    except:
        return render_template("index.html", result="Invalid Input")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

