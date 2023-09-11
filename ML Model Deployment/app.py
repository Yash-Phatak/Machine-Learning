#Contains the Flask Code
import numpy as np
import pickle
from flask import render_template,jsonify,Flask,request

#Create Flask App
app = Flask(__name__)

model = pickle.load(open("ML Model Deployment/model.pkl","rb"))
@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict",methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features  = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("index.html",prediction_text = "The Flower Species is {}".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)