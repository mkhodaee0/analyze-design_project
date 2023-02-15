import requests
import json
from pymongo import MongoClient

print("1- sign in\n2- sign up user")
number = int(input("Please input a number: "))
client = MongoClient('mongodb://localhost:27017/')
db = client["store"]
col = db["user"]

if number == 1:
    username = input("Please input username: ")
    password = input("Please input password: ")
    query1 = {"username": username, "password": password}
    doc = col.find(query1)
    for i in doc:
        query2 = {"status": "disconnect"}
        newvalues = {"$set": {"status": "connect"}}
        doc.update_one(query2, newvalues)

if number == 2:
    username = input("Please input username: ")
    password = input("Please input password: ")
    email = input("Please input email: ")

    dictionary = {"username": username, "password": password, "email": email}
    x = col.insert_one(dictionary)



# POST for user
#api_url = "https://localhost:8000/api/v0/signup"
#with open("user.json", "r") as read_file:
#    data = json.load(read_file)

#response = requests.post(api_url, json=data)
#response.json()