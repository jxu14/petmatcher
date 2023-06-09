# Author: Seok Hee Hong

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
party = int(form.getvalue('party'))
affection = int(form.getvalue('affection'))
nap = int(form.getvalue('nap'))
socialize = int(form.getvalue('socialize'))
lively = int(form.getvalue('lively'))
challenge = int(form.getvalue('challenge'))

# calculate scores for each animal based on user input
dog_score = party + affection + lively + challenge
cat_score = affection + nap + socialize + challenge

# calculate overall scores and percentages
total_score = dog_score + cat_score
dog_percentage = round(dog_score / total_score * 100, 1)
cat_percentage = round(cat_score / total_score * 100, 1)

# determine which animal to suggest based on scores
dog_scores = {
    'French Bulldog': 0.15 * lively + 0.15 * socialize + 0.1 * party + 0.2 * affection + 0.1 * challenge + 0.15 * nap,
    'Labrador Retriever': 0.1 * lively + 0.1 * socialize + 0.1 * party + 0.15 * affection + 0.2 * challenge + 0.25 * nap,
    'Golden Retriever': 0.1 * lively + 0.1 * socialize + 0.15 * party + 0.15 * affection + 0.15 * challenge + 0.25 * nap,
    'German Shepherd Dog': 0.1 * lively + 0.1 * socialize + 0.15 * party + 0.2 * affection + 0.1 * challenge + 0.25 * nap,
    'Poodle': 0.15 * lively + 0.1 * socialize + 0.1 * party + 0.2 * affection + 0.1 * challenge + 0.25 * nap,
    'American Bulldog': 0.1 * lively + 0.05 * socialize + 0.15 * party + 0.15 * affection + 0.25 * challenge + 0.25 * nap,
    'Rottweiler': 0.1 * lively + 0.1 * socialize + 0.1 * party + 0.15 * affection + 0.25 * challenge + 0.25 * nap,
    'Beagle': 0.1 * lively + 0.2 * socialize + 0.2 * party + 0.15 * affection + 0.1 * challenge + 0.25 * nap,
    'Dachshund': 0.1 * lively + 0.15 * socialize + 0.1 * party + 0.15 * affection + 0.15 * challenge + 0.35 * nap,
    'German Shorthaired Pointer': 0.2 * lively + 0.2 * socialize + 0.1 * party + 0.15 * affection + 0.1 * challenge + 0.25 * nap
}

cat_scores = {
    'Exotic Shorthair': 0.2 * affection + 0.2 * nap + 0.1 * socialize + 0.1 * challenge,
    'Ragdoll': 0.15 * affection + 0.3 * nap + 0.1 * socialize + 0.1 * challenge + 0.05 * lively + 0.05 * party,
    'British Shorthair': 0.1 * affection + 0.25 * nap + 0.1 * socialize + 0.15 * challenge + 0.1 * lively + 0.1 * party,
    'Persian': 0.2 * affection + 0.3 * nap + 0.05 * socialize + 0.05 * challenge,
    'Maine Coon': 0.15 * affection + 0.2 * nap + 0.15 * socialize + 0.1 * challenge + 0.1 * lively + 0.1 * party,
    'American Shorthair': 0.15 * affection + 0.2 * nap + 0.2 * socialize + 0.1 * challenge + 0.1 * lively + 0.05 * party,
    'Scottish Fold': 0.1 * affection + 0.2 * nap + 0.2 * socialize + 0.1 * challenge + 0.15 * lively + 0.05 * party,
    'Sphynx': 0.15 * affection + 0.2 * nap + 0.1 * socialize + 0.2 * challenge + 0.1 * lively + 0.05 * party,
    'Abyssinian': 0.2 * affection + 0.15 * nap + 0.2 * socialize + 0.15 * challenge + 0.1 * lively + 0.1 * party,
    'Devon Rex': 0.2 * affection + 0.2 * nap + 0.1 * socialize + 0.1 * challenge + 0.1 * lively + 0.1 * party
}

# Sort and grab top (three)
top_dogs = sorted(dog_scores, key=dog_scores.get, reverse=True)[:3]
top_cats = sorted(cat_scores, key=cat_scores.get, reverse=True)[:3]

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

def are_you_dog_or_cat():
    if dog_percentage > cat_percentage:
        person = 'a dog'
    elif cat_percentage > dog_percentage:
        person = 'a cat'
    else:
        person = 'both a dog and cat'
    return f'''
        <div align="center">
            <div style="display: flex; flex-direction: column; align-items: center; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); padding: 2rem; width: 80%; background-color: #fff;">
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <h1 style="font-size: 2.5rem; margin-bottom: 1rem;">Pet Suggestion Results</h1>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1.5rem;">According to your answers, you are {person} person!</h3>
                    <div style="display: flex; align-items: center; justify-content: center; width: 100%; max-width: 600px;">
                        <div style="background-color: #97A3DC; height: 2rem; width: { dog_percentage }%;"></div>
                        <div style="background-color: #8D5EB0; height: 2rem; width: { cat_percentage }%;"></div>
                    </div>
                    <div style="display: flex; align-items: center; justify-content: center; width: 100%; max-width: 600px;">
                    <h3 style="font-size: 1.5rem; margin-left: 1rem;">{ dog_percentage }% Dog</h3>
                        <h3 style="font-size: 1.5rem; margin-left: 1rem;">{ cat_percentage }% Cat</h3>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 1.5rem;">
                        <h4 style="font-size: 1.25rem; margin-bottom: 0.75rem;">Based on your answers, we suggest you adopt a { top_dogs[0] } or a { top_cats[0] }!</h4>
                        <h4 style="font-size: 1.25rem; margin-bottom: 0.75rem;">Other dog suggestions include a { top_dogs[1] } or a { top_dogs[2] }.</h4>
                        <h4 style="font-size: 1.25rem;">Other cat suggestions include a { top_cats[1] } or a { top_cats[2] }.</h4>
                    </div>
                </div>
            </div>
        </div>
        '''

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

    if dog_percentage > cat_percentage:
        params = {
            "type": "Dog",
            "breed": top_dogs[0],
        }
    else:
        params = {
            "type": "Cat",
            "breed": top_cats[0],
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
            continue
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
                <div class="pet-listing">
                    <h2 class="pet-name">{name}</h2>
                    <p class="pet-description">{description}</p>
                    <div class="pet-photo-wrapper">
                        <img class="pet-photo" src="{photo}">
                    </div>
                    <ul class="pet-details">
                        <li><strong>Type:</strong> {animal_type}</li>
                        <li><strong>Primary Breed:</strong> {primary_breed}</li>
                        <li><strong>Age:</strong> {age}</li>
                        <li><strong>Gender:</strong> {gender}</li>
                    </ul>
                    <div class="contact-info">
                        <h3>Contact Info</h3>
                        <ul>
                        <li><strong>Email:</strong> href="mailto:{email}"{email}</li>
                        <li><strong>Phone:</strong> {phone}</li>
                        <li><strong>Address:</strong> {formatted_address}</li>
                        </ul>
                    </div>
                    <a class="learn-more-link" href="{link}">Learn more about {name}</a>
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
print(are_you_dog_or_cat())
# print("<h1>PetMatcher Results:</h1>")
# print("<p>Living place: " + str(living) + "</p>")
# print("<p>Space for pet: " + str(space) + "</p>")
# print("<p>Living style: " + str(lifestyle) + "</p>")
# print("<p>Budget: " + str(budget) + "</p>")
# print("<p>Allergies: " + str(allergies) + "</p>")
# print("<p>Hours available: " + str(hours) + "</p>")
# print("<p>Promise: " + str(promise) + "</p>")
print(format_animals(animals))
print("</body>")
print("</html>")
