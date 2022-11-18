import requests
import numpy as np
from flask import Flask, render_template, request, jsonify

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "UPWRFTFhkvYA6wNCvrVT21hKgkcyyWYJTLut7wa6eSRu"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/index.html')
def home1():
    return render_template("index.html")


@app.route('/new.html')
def home2():
    return render_template("new.html")

@app.route('/login',methods=['POST','GET'])
def login():
 if request.method == 'POST':
    x=str(request.form['year'])
    x=x.split(',')
    print(x)
    for w in range(0, len(x)):
        x[w]=float(x[w])
    print(x)
    t=[[ [x[0]], [x[1]], [x[2]], [x[3]], [x[4]], [x[5]], [x[6]], [x[7]], [x[8]], [x[9]]]]
    payload_scoring = {
    "input_data": [{"field": [[["i1"], ["i2"], ["i3"], ["i4"], ["i5"], ["i6"], ["i7"], ["i8"], ["i9"], ["1i0"]]],

                     "values":t }]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/f73b8e94-628a-4cd8-8a84-a5b527eb1468/predictions?version=2022-11-17', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    predictions=response_scoring.json()
    print("predicted value is")
    print(predictions['predictions'][0]['values'][0][0])
    pred=predictions['predictions'][0]['values'][0][0]

    return render_template("result.html",result=str(pred))

if __name__=='__main__':
  app.run(debug=True, port=5000)