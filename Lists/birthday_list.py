###24/20/2018
# Author: Rene Cortez
# How to edit list

# Creating a list of months
birthday_months = ['spril', 'may', 'november']

print(birthday_months)

# Changing an element of list
birthday_months[0] = 'april'

print(birthday_months)

# using append method
birthday_months.append('june')

print(birthday_months)

#creating an empty list
birthday_months = []

print(birthday_months)

birthday_months.append('august')

print(birthday_months)

# Using the insert method
birthday_months.insert(0, 'may')

print(birthday_months)

# using delete statement
del birthday_months[1]

print(birthday_months)
