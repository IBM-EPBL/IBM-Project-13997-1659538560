import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "UPWRFTFhkvYA6wNCvrVT21hKgkcyyWYJTLut7wa6eSRu"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [[["i1"],["i2"],["i3"],["i4"],["i5"],["i6"],["i7"],["i8"],["i9"],["1i0"]]],

                                   "values": [[[0.47567],[0.908889],[0.4783956],[0.9876],[0.839099],[0.43827895],[0.473525],[0.750590],[0.567745],[0.98766]]]}]}



response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/f73b8e94-628a-4cd8-8a84-a5b527eb1468/predictions?version=2022-11-17', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
predictions=response_scoring.json()
print("predicted value is")
print(predictions['predictions'][0]['values'][0][0])