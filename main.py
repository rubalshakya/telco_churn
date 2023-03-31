from flask import Flask,request,jsonify,render_template
from Project_app.utils import Churn

app = Flask(__name__)



@app.route("/")
def Home():
    return render_template("home.html")


@app.route("/predict", methods=["post"])
def Predict_churn():
    data = request.form
    Churn_inst = Churn(data)
    res = Churn_inst.predict_churn()
    print(res)
    return render_template("result.html",Result = res)

app.run(debug=True)
    




