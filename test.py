import requests
import json

# Define the API endpoint
url = "https://v6yotphfeti3oktsj4sj722xjy0biugx.lambda-url.us-east-1.on.aws/"

js_url = "https://j7bck3k74fxw3dqmtpna63yyci0qtgmj.lambda-url.us-east-1.on.aws/"

# Define the JSON payload
payload = {
    "data": json.dumps ({"key": "This is the body of the text"}),
}

# Convert the payload to JSON format
data = json.dumps(payload)

# Send a POST request to the API endpoint with the JSON payload
response = requests.post(url, data=data, headers={'Content-Type': 'application/json'})

# Print the response from the server
print(response.text)