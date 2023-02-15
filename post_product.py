import requests
import json
from pymongo import MongoClient

print("1- register product\n2- Edit name product\n3- delete product\n4- search in products")
number = int(input("Please input a number: "))
client = MongoClient('mongodb://localhost:27017/')
db = client["store"]
col = db["product"]

if number == 1:
  name = input('please input a laptop name: ')
  brand = input('please input a laptop brand: ')
  price = int(input('please input a laptop price: '))
  category = input('please input a laptop category: ')

  dictionary = {"name": name, "brand": brand, "price": price, "category": category}
  x = col.insert_one(dictionary)

if number == 2:
  old_name = input("Please input a current laptop name: ")
  new_name = input("Please input the name that you want: ")
  query = {"name": old_name}
  newvalues = {"$set": {"name": new_name}}

  col.update_one(query, newvalues)

if number == 3:
  delete_product = input("Please input the name of that product that you want to delete")

  query = {"name": delete_product}
  col.delete_one(query)

if number == 4:
  print("Searching by:\n1- name\n2- brand\n3- price\n3- category")
  numb1 = input("Please input a number: ")

  if numb1 == 1:
    product_name = input("Please input the name of that product you want: ")
    query = {"name": product_name}
    doc = col.find(query)

    for i in doc:
      print(i)

  if numb1 == 2:
    product_brand = input("Please input the brand of that products you want:")
    query = {"brand": product_brand}
    doc = col.find(query)

    for i in doc:
      print(i)

  if numb1 == 3:
    product_price = int(input("Please input the price of that products you want:"))
    query = {"price": product_price}
    doc = col.find(query)

    for i in doc:
      print(i)

  if numb1 == 4:
    product_category = input("Please input the category of that products you want:")
    query = {"category": product_category}
    doc = col.find(query)

    for i in doc:
      print(i)

# POST for product
#api_url = "https://localhost:8000/api/v0/product"
#with open("product.json", "r") as read_file:
#    data = json.load(read_file)

#response = requests.post(api_url, json=data)
#response.json()