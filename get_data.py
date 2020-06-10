import requests
import json
import statistics

print("REQUESTING SOME DATA FROM THE INTERNET...")

###
# Write a python program which issues a GET request for this product.json data, 
# then prints the product's "name".
###

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
response = requests.get(request_url)
#print(response.status_code)
#print(response.text)

products = json.loads(response.text)
product = products["name"]
print("product", product)

###
# Write a Python program which issues a GET request for this products.json data,
# then loop through each product and print its "name" and "id" attributes.
###

request_url2 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
otherproducts = requests.get(request_url2)
listprods = json.loads(otherproducts.text)

#print(listprods)

nameid = []
#
#for p in listprods:
#    x = p["name"]
#    y = p["id"]
#    #z = zip(x,y)
#    nameid.append(x)
#    nameid.append(y)
for p in listprods:
    print(p["name"],p["id"])

#print("nameid", nameid)

###
# Write a Python program which issues a GET request for this gradebook.json data, 
# then calculate and print the average, min, and max grades.
###

request_url3 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
grades = requests.get(request_url3)
listgrades = json.loads(grades.text)

students = listgrades["students"]
#print("students",students)

grades = []

for i in students:
    i["finalGrade"] = float(i["finalGrade"])
    grades.append(i["finalGrade"])

avg = statistics.mean(grades)
mingrades = min(grades)
maxgrades = max(grades)

#print(grades)
print("average", avg)
print("minimum",mingrades)
print("maximum", maxgrades)
