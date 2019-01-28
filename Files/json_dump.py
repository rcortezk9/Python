# Working with json.dump() function

import json

phone_numbers = [123456789]

filename = 'phone_numbers.json'
with open(filename, 'w') as file_object:
    json.dump(phone_numbers, file_object)
