#!/usr/bin/env python3
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
city = form.getvalue('city')
city = str(city).capitalize()
state = form.getvalue('state')
state = str(state)
space = form.getvalue('space')
lifestyle = form.getvalue('lifestyle')
budget = form.getvalue('budget')
allergies = form.getvalue('allergies')
hours = form.getvalue('hours')
promise = form.getvalue('promise')

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
        return data['animals'][:3]
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

        # format the information in a box
        box = f'''
            <div style="border: 1px solid black; padding: 10px; margin-bottom: 10px;">
                <h3>{name}</h3>
                <p>{description}</p>
                <img src="{photo}" style="max-width: 300px;">
                <p>Type: {animal_type}</p>
                <p>Primary Breed: {primary_breed}</p>
                <p>Age: {age}</p>
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
print("<title>PetFinder Results:</title>")
print("</head>")
print("<body>")
print("<h1>PetFinder Results</h1>")
print("<p>City: " + city + "</p>")
print("<p>State: " + state + "</p>")
print("<p>Space for pet: " + str(space) + "</p>")
print("<p>Living style: " + str(lifestyle) + "</p>")
print("<p>Budget: " + str(budget) + "</p>")
print("<p>Allergies: " + str(allergies) + "</p>")
print("<p>Hours available: " + str(hours) + "</p>")
print("<p>Promise: " + str(promise) + "</p>")
print(format_animals(animals))
print("</body>")
print("</html>")