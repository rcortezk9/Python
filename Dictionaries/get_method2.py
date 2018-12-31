# Editing & deleting values in a dictionary

# terms = {'interger' : 'Is a number that contains a decimal place.'}
#
# terms ['interger'] = 'A whole value'
#
# print(terms.get('interger'))

terms = {'interger' : 'Is a number that contains a decimal place.', 'string' : 'A sequence of characters.'}

del terms['interger']

print(terms)
