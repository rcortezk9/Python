# Working with json.load() function

import json

filename = 'phone_numbers.json'

with open(filename) as file_object:
    phone_numbers = json.load(file_object) # Load file back into memory

print (phone_numbers)
