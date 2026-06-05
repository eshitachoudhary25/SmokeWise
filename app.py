from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/assessment")
def assessment():
    return render_template("assessment.html")

@app.route("/result", methods=["POST"])
def result():
    print("FILES IN TEMPLATES:", os.listdir("templates"))

    name = request.form["name"]
    age = int(request.form.get("age", 0))
    height = float(request.form.get("height", 0))
    weight = float(request.form.get("weight", 0))
    cigarettes = int(request.form.get("cigarettes", 0))
    years = int(request.form.get("years", 0))
    exercise = int(request.form.get("exercise", 0))

    # BMI calculation
    bmi = weight / ((height / 100) ** 2)

    # Risk score
    risk_score = (cigarettes * 2) + (years * 3) - (exercise * 2)
    health_score = 100 - risk_score
    if health_score < 0:
        health_score = 0
    if health_score > 100:
        health_score = 100    

    # Risk level
    if risk_score < 20:
        risk_level = "Low Risk"
    elif risk_score < 50:
        risk_level = "Moderate Risk"
    else:
        risk_level = "High Risk"

    # IMPORTANT: default value (THIS FIXES YOUR ERROR)
    recommendation = "Take care of your health"

    if risk_level == "Low Risk":
        recommendation = "Maintain your healthy habits."

    elif risk_level == "Moderate Risk":
        recommendation = "Reduce smoking and increase exercise."

    else:
        recommendation = "High risk detected. Consider quitting smoking and consult a doctor."
    print(recommendation)
    print("Debug:",recommendation)
    return render_template(
        "result.html",
        name=name,
        age=age,
        bmi=round(bmi, 2),
        risk_score=risk_score,
        risk_level=risk_level,
        recommendation=recommendation,
        health_score=health_score 
    )
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
