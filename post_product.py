import requests
import json

# POST for product
api_url = "https://localhost:8000/api/v0/product"
with open("product.json", "r") as read_file:
    data = json.load(read_file)

response = requests.post(api_url, json=data)
response.json()