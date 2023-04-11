# #!/usr/bin/env python3

# import cgi
# import cgitb
# import requests
# import json

# cgitb.enable()

# # Get the form data from the HTTP request
# form = cgi.FieldStorage()

# # Get the answers to the questions
# living = form.getvalue('living')
# space = form.getvalue('space')
# lifestyle = form.getvalue('lifestyle')
# budget = form.getvalue('budget')
# allergies = form.getvalue('allergies')
# hours = form.getvalue('hours')
# promise = form.getvalue('promise')

# ### Match answer to tags
# # set size based on living space
# if living == 'house':
#     animal_size = 'Large, Xlarge'
# elif living == 'apartment':
#     animal_size = 'Small, Medium'
#     animal_house_trained = 1
    
# # set size based on space
# if space == 'corner':
#     animal_size = 'Small'
    
# # set tags based on lifestyle -- excluded for now

# # exclude certain types based on allergies - excluded for now

# API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJZY1NkRmhZZHdrZUpTUU9rMzlQV1VuSnJCZlZtQVpJcm81MVVkeWhFSjBNY1FtaWwxTyIsImp0aSI6Ijk0OGRjMzIwMDIyNjFlOTliNDI3ZDgzZGIxZGRiOTgzNTQ2YzkzZDQwMjA2YzBiZjAxNzJhMjE0MGUzYTRhN2M4NTMxMWI0Njk5NmU5MDJiIiwiaWF0IjoxNjgwNTc1MTgxLCJuYmYiOjE2ODA1NzUxODEsImV4cCI6MTY4MDU3ODc4MSwic3ViIjoiIiwic2NvcGVzIjpbXX0.rS80tuH0j3ETpkwdM-E6b7LSJLXFbLQOM5TIJ3Za1k9IXX98MFN2zItCWC68NMocERm18Ehx44BgA1lM_3KRwdjmpBtY7nqPlbqRLzTH4BTjYITK97eI0j4wk2qG_L8OVzTAQ7L59TyaYuVoFARGOfDNgTJ_xkWdynSAN9gjJOYBDiA_I4425dydo4zW5N5stWdnUQAX43wao1A2E05Vgg60tKpOIxEfaxmzWqG8_XC3muc6eVWf9nePgbu4XwQxr7r5qlVWm57oAyXJEkKBdAkYAi1YDoPwNZ55CIjTBWoAwPQDhL_01mG4D9eRToz38_SGbIpEcuHU5MtAKjd7nw"

# headers = {
#     "Authorization": f"Bearer {API_TOKEN}"
# }

# params = {
#     # "size": animal_size,
# }

# response = requests.get("https://api.petfinder.com/v2/animals", headers=headers, params=params)

# data = json.loads(response.text)

# # extract the first three animals
# animals = data['animals'][:3]

# # get info
# all_matches = ''
# animal_names = set()
# for animal in animals:
#     name = animal['name']
#     if name in animal_names:
#         continue # skip this animal if we've already seen it
#     animal_names.add(name) 
#     description = animal['description']
#     if animal['photos']:
#         photo = animal['photos'][0]['medium']
#     else:
#         photo = 'No photo available'
#     animal_type = animal['type']
#     primary_breed = animal['breeds']['primary']
#     age = animal['age']
    
#     # format the information in a box
#     box = f'''
#         <div style="border: 1px solid black; padding: 10px; margin-bottom: 10px;">
#             <h3>{name}</h3>
#             <p>{description}</p>
#             <img src="{photo}" style="max-width: 300px;">
#             <p>Type: {animal_type}</p>
#             <p>Primary Breed: {primary_breed}</p>
#             <p>Age: {age}</p>
#         </div>
#     '''
    
#     all_matches += box

# # Print the answers
# print("Content-Type: text/html")    # Set the content type of the response
# print()    # Print an empty line to indicate the end of the headers
# print("<html>")
# print("<head>")
# print("<title>Pet Finder Results</title>")
# print("</head>")
# print("<body>")
# print("<h1>Pet Finder Results</h1>")
# print("<p>Living place: " + str(living) + "</p>")
# print("<p>Space for pet: " + str(space) + "</p>")
# print("<p>Living style: " + str(lifestyle) + "</p>")
# print("<p>Budget: " + str(budget) + "</p>")
# print("<p>Allergies: " + str(allergies) + "</p>")
# print("<p>Hours available: " + str(hours) + "</p>")
# print("<p>Promise: " + str(promise) + "</p>")
# print(all_matches)
# print("</body>")
# print("</html>")



# #!/usr/bin/env python3

# import cgi
# import cgitb
# import requests
# import json

# cgitb.enable()

# # Get the form data from the HTTP request
# form = cgi.FieldStorage()

# # Get the answers to the questions
# living = form.getvalue('living')
# space = form.getvalue('space')
# lifestyle = form.getvalue('lifestyle')
# budget = form.getvalue('budget')
# allergies = form.getvalue('allergies')
# hours = form.getvalue('hours')
# promise = form.getvalue('promise')

# ### Match answer to tags
# # set size based on living space
# if living == 'house':
#     animal_size = 'Large, Xlarge'
# elif living == 'apartment':
#     animal_size = 'Small, Medium'
#     animal_house_trained = 1

# # set size based on space
# if space == 'corner':
#     animal_size = 'Small'

# # set tags based on lifestyle -- excluded for now

# # exclude certain types based on allergies - excluded for now

# API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJZY1NkRmhZZHdrZUpTUU9rMzlQV1VuSnJCZlZtQVpJcm81MVVkeWhFSjBNY1FtaWwxTyIsImp0aSI6IjJhNzc3NzJlMTFkMDdjYzk5MWZjYzRkNWJhYmM0ZDhjNjI2OGFiMmE0YTM0MDg1ODNkMDdlMzQ5ZGE5NjdmMGE5OTcwYjQwZTZlM2JmYWQxIiwiaWF0IjoxNjgwNTg0MDExLCJuYmYiOjE2ODA1ODQwMTEsImV4cCI6MTY4MDU4NzYxMSwic3ViIjoiIiwic2NvcGVzIjpbXX0.NHdnH4yd_Ir4S6IOP20D8NI8xpHaiyfSj3zTxV7L9c1NBuvxODUJMOFaEye3T80hY2tgusfrbvL-US90lXsj7qgW4yZr7HXwoA49YLqVU0o7Qgvurq_yvuEldCL_I_OuRb_Fb1doe9bbsq4TxhR8gVHzJd3wIw0PsOx__BPlvw8JHEX2WAuGvgWB22ge5AXLlkT_KDH7CrJwEAka__dD5eLogM1kIEbgcDix52P27L2V7kFzeG_Fl8vBQto7T9mIeQhzuUhCUyWLT9KzJ8s4uGyCgG9iEBPYaPXBeVhyy_fK0lEFVDy_zha_JCsta1XpHGIPotwqvJUXwE6xlsVeAg"

# headers = {
#     "Authorization": f"Bearer {API_TOKEN}"
# }

# params = {
#     # "size": animal_size,
# }
# response = requests.get("https://api.petfinder.com/v2/animals", headers=headers, params=params)

# data = json.loads(response.text)

# # extract the first three animals
# animals = data['animals'][:3]

# # get info
# all_matches = ''
# animal_names = set()
# for animal in animals:
#     name = animal['name']
#     if name in animal_names:
#         continue # skip this animal if we've already seen it
#     animal_names.add(name)
#     description = animal['description']
#     if animal['photos']:
#         photo = animal['photos'][0]['medium']
#     else:
#         photo = 'No photo available'
#     animal_type = animal['type']
#     primary_breed = animal['breeds']['primary']
#     age = animal['age']

#     # format the information in a box
#     box = f'''
#         <div style="border: 1px solid black; padding: 10px; margin-bottom: 10px;">
#             <h3>{name}</h3>
#             <p>{description}</p>
#             <img src="{photo}" style="max-width: 300px;">
#             <p>Type: {animal_type}</p>
#             <p>Primary Breed: {primary_breed}</p>
#             <p>Age: {age}</p>
#         </div>
#     '''

#     all_matches += box

# # Print the answers
# print("Content-Type: text/html")    # Set the content type of the response
# print()    # Print an empty line to indicate the end of the headers
# print("<html>")
# print("<head>")
# print("<title>Pet Finder Results</title>")
# print("</head>")
# print("<body>")
# print("<h1>Pet Finder Results</h1>")
# print("<p>Living place: " + str(living) + "</p>")
# print("<p>Space for pet: " + str(space) + "</p>")
# print("<p>Living style: " + str(lifestyle) + "</p>")
# print("<p>Budget: " + str(budget) + "</p>")
# print("<p>Allergies: " + str(allergies) + "</p>")
# print("<p>Hours available: " + str(hours) + "</p>")
# print("<p>Promise: " + str(promise) + "</p>")
# print(all_matches)
# print("</body>")
# print("</html>")

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
print("<title>Pet Finder Results</title>")
print("</head>")
print("<body>")
print("<h1>Pet Finder Results</h1>")
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