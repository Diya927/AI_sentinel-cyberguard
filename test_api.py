import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "packet_size": 1500,
    "failed_logins": 5,
    "request_frequency": 250
}

response = requests.post(url, json=data)

print("Response from API:", response.json())