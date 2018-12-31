# Using get() method with a dictionary

#
terms = {'interger' : 'A whole number.'}
print(terms.get('interger'))

# To use the get method you have to use key value
print(terms.get('float', 'Not in the dictionary'))
