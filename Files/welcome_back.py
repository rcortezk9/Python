# Storing and reading user data

import json

filename = 'username.json'

try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("What is your username? ")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        print("Thank you, I will remeber you when you come back.")
else:
    print("Welcome back, " + username + "!")
