from pymongo import MongoClient

myclient = MongoClient('mongodb://localhost:27017/')
mydb = myclient["store"]
mycol = mydb["transaction"]

product = input("Please input product name: ")
username = input("Please input username: ")
status = input("Please input the buying status: ")

mydict = {"product": product, "username": username, "status": status}
x = mycol.insert_one(mydict)