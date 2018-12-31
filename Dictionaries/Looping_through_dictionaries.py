# Looping througha dictionary

birthday_months = {
    'rene' : 'january',
    'stephanie' : 'May',
    'mariah' : 'october',
}

for key, value in birthday_months.items():
    print("\nName: " + key)
    print("Months: " + value)

#Looping through key value pairs
book_1 = {
    'name' : 'elon musk',
    'author' : 'ashlee vance',
    'price' : '14.99',
    'publisher' : 'virgin books',
}

for key, value in book_1.items():
    print("\nKey: " + key)
    print("Value: " + value)
