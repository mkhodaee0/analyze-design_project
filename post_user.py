import requests
import json

# POST for user
api_url = "https://localhost:8000/api/v0/signup"
with open("user.json", "r") as read_file:
    data = json.load(read_file)

response = requests.post(api_url, json=data)
response.json()