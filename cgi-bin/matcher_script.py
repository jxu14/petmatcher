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
living = form.getvalue('living')
space = form.getvalue('space')
lifestyle = form.getvalue('lifestyle')
budget = form.getvalue('budget')
allergies = form.getvalue('allergies')
hours = form.getvalue('hours')
promise = form.getvalue('promise')

# answers with scale of 1-5
party = form.getvalue('party')
affection = form.getvalue('affection')
nap = form.getvalue('nap')
socialize = form.getvalue('socialize')
lively = form.getvalue('lively')
challenge = form.getvalue('challenge')

# calculate scores for each animal based on user input
dog_score = party + affection + lively + challenge
cat_score = affection + nap + socialize + challenge

# determine which animal to suggest based on scores
# if dog_score > cat_score:
#     # get a dog
# else:
#     # get a cat


### Match answer to tags
# set size based on living space
if living == 'house':
    animal_size = 'Large, Xlarge'
elif living == 'apartment':
    animal_size = 'Small, Medium'
    animal_house_trained = 1

# set size based on space
if space == 'corner':
    animal_size = 'Small'

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
        link = animal['url']
        gender = animal['gender']
        contact = animal['contact']
        email = contact['email']
        phone = contact['phone']
        address = contact['address']
        conv = lambda i: i or ''
        street_num = conv(address['address1'])
        formatted_address = street_num + " " + str(address['city']) + ", " + str(address['state']) + " " + str(address['postcode'])


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
print("<title>PetMatcher Results</title>")
print("</head>")
print("<body>")
print("<a href=\"/index.html\"><img src=\"https://i.imgur.com/AFDeZ98.png\" alt=\"PetMatcher\" class=\"logo\"></a>")
print("<h1>PetMatcher Results:</h1>")
print("<p>Living place: " + str(living) + "</p>")
print("<p>Space for pet: " + str(space) + "</p>")
print("<p>Living style: " + str(lifestyle) + "</p>")
print("<p>Budget: " + str(budget) + "</p>")
print("<p>Allergies: " + str(allergies) + "</p>")
print("<p>Hours available: " + str(hours) + "</p>")
print("<p>Promise: " + str(promise) + "</p>")
print(format_animals(animals))
print("</body>")
print("</html>")
