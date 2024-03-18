from flask import render_template, url_for, flash, redirect,request,send_file,jsonify
import requests
from Water import app

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/predict_potability", methods=["POST"])
def predict_potability():
    if request.method == "POST":
        ph = float(request.form["ph"])
        Hardness = float(request.form["Hardness"])
        Solids = float(request.form["Solids"])
        Chloramines = float(request.form["Chloramines"])
        Sulfate = float(request.form["Sulfate"])
        Conductivity = float(request.form["Conductivity"])
        Organic_carbon = float(request.form["Organic_carbon"])
        Trihalomethanes = float(request.form["Trihalomethanes"])
        Turbidity = float(request.form["Turbidity"])

        # Prepare data for API request (assuming the format)
        data = {
            "data": [ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, 
                      Organic_carbon, Trihalomethanes, Turbidity]
        }
        url = "https://kingsengg-edu.ap-south-1.modelbit.com/v1/predict_water_potability/latest"
        # Send POST request to the API
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, json=data)

        # Check for successful response
        if response.status_code == 200:
            response_json = response.json()
            # Process and display the prediction result (optional)
            # You can extract the probability or classification from the response here
            return render_template("water_quality_result.html", prediction=response_json)
        else:
            error_message = f"Error: API request failed with status code {response.status_code}"
            return render_template("water_quality_result.html", error=error_message)

    return "Invalid request method"  # Handle non-POST requests