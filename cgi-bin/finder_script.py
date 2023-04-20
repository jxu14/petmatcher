# Author: Anne Kuckertz

#!/usr/bin/env python
import cgi
import cgitb
import requests
import json
import time
import subprocess

cgitb.enable()

# Get the form data from the HTTP request
form = cgi.FieldStorage()

# Get the answers to the questions
type = form.getvalue('type')
if type == "Other":
    type = "Small & Furry"
if type=="Dog" or type=="Cat":
    kids = form.getvalue('kids')
city = form.getvalue('city')
city = str(city).capitalize()
state = form.getvalue('state')
state = str(state)
distance = form.getvalue('distance')

age = form.getvalue('age')

declawed = form.getvalue('declawed')
special_needs = form.getvalue('needs')
breed = form.getvalue('breed')

API_TOKEN = None

def get_token():
    global API_TOKEN
    url = "https://api.petfinder.com/v2/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": "YcSdFhYdwkeJSQOk39PWUnJrBfVmAZIro51UdyhEJ0McQmil1O",
        "client_secret": "yEEZzcE7qW4g041ebddXCc7mPpmSNCjw4TVHYQL0"
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        API_TOKEN = json.loads(response.text)['access_token']
        return True
    else:
        return False

def get_animals():
    global API_TOKEN
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    if type == "Dog" or type == "Cat":
        params = {
            "type": type,
            "location": city + ", " + state,
            "distance": distance,
            "breed": breed,
            "age": age,
            "kids": kids,
            "declawed": declawed,
            "special_needs": special_needs,
        }
    else:
        params = {
            "type": type,
            "location": city + ", " + state,
            "distance": distance,
            "breed": breed,
            "age": age,
            "declawed": declawed,
            "special_needs": special_needs,
        }
    response = requests.get("https://api.petfinder.com/v2/animals", headers=headers, params=params)
    if response.status_code == 401:
        if get_token():
            headers = {
                "Authorization": f"Bearer {API_TOKEN}"
            }
            response = requests.get("https://api.petfinder.com/v2/animals", headers=headers, params=params)
        else:
            return None
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['animals'][:20]
    else:
        return None
def format_animals(animals):
    all_matches = ''
    animal_names = set()
    for animal in animals:
        name = animal['name']
        if name in animal_names:
            continue # skip this animal if we've already seen it
        animal_names.add(name)
        description = animal['description']
        if animal['photos']:
            photo = animal['photos'][0]['medium']
        else:
            photo = 'No photo available'

        animal_type = animal['type']
        primary_breed = animal['breeds']['primary']
        age = animal['age']
        link = animal['url']
        gender = animal['gender']
        contact = animal['contact']
        email = contact['email']
        phone = contact['phone']
        address = contact['address']
        conv = lambda i: i or ''
        street_num = conv(address['address1'])
        formatted_address = street_num + " " + str(address['city']) + ", " + str(address['state']) + " " + str(
            address['postcode'])

        # format the information in a box
        box = f'''
            <div style="border: 1px solid black; padding: 10px; margin-bottom: 10px;">
                <h3>{name}</h3>
                <p>{description}</p>
                <img src="{photo}" style="max-width: 300px;">
                <p>Type: {animal_type}</p>
                <p>Primary Breed: {primary_breed}</p>
                <p>Age: {age}</p>
                <p>Gender: {gender} </p>
                <h3>Contact info</h3>
                <span>&ensp;Email: {email} </span>
                <br>
                <span>&ensp;Phone Number: {phone} </span>
                <br>
                <span>&ensp;Address: {formatted_address} </span>
                <br>
                <br>
                <a href="{link}">Click here to learn more about {name}</a>
            </div>
        '''

        all_matches += box
    return all_matches
# get info
animals = get_animals()

# Print the answers
print("Content-Type: text/html")    # Set the content type of the response
print()    # Print an empty line to indicate the end of the headers
print("<html>")
print("<head>")
print("<link rel=\"stylesheet\" type=\"text/css\" href=\"../styles.css\" media=\"screen\"/>")
print("<title>PetFinder Results</title>")
print("</head>")
print("<hr>")
print("<body>")
print("<a href=\"/index.html\"><img src=\"https://i.imgur.com/AFDeZ98.png\" alt=\"PetMatcher\" class=\"logo\"></a>")
print("<h1>PetFinder Results:</h1>")
print(format_animals(animals))
if not animals:
    print("<h2>Sorry there aren't any matches for your search. :( Maybe if you try again with different parameters you will find your new best friend!</h2>")
print("</body>")
print("</html>")

