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
city = form.getvalue('city')
city = str(city).capitalize()
state = form.getvalue('state')
state = str(state)
distance = form.getvalue('distance')

age = form.getvalue('age')

declawed = form.getvalue('declawed')
special_needs = form.getvalue('needs')
breed = form.getvalue('breed')
# space = form.getvalue('space')
# lifestyle = form.getvalue('lifestyle')
# budget = form.getvalue('budget')
# allergies = form.getvalue('allergies')
# hours = form.getvalue('hours')
# promise = form.getvalue('promise')


# set tags based on lifestyle -- excluded for now

# exclude certain types based on allergies - excluded for now
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
    params = {
        # "size": animal_size,
        "type": type,
        "location": city + ", " + state,
        "distance": distance,
        "breed": breed,
        #add age, given that the user could have multiple ages selected
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
# print("<p>City: " + city + "</p>")
# print("<p>State: " + state + "</p>")
# print("<p>Space for pet: " + str(space) + "</p>")
# print("<p>Living style: " + str(lifestyle) + "</p>")
# print("<p>Budget: " + str(budget) + "</p>")
# print("<p>Allergies: " + str(allergies) + "</p>")
# print("<p>Hours available: " + str(hours) + "</p>")
# print("<p>Promise: " + str(promise) + "</p>")
print(format_animals(animals))
print("</body>")
print("</html>")

