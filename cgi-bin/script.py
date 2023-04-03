#!/usr/bin/env python3

import cgi
import cgitb
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
print("</body>")
print("</html>")
