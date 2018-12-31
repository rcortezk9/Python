#  Using a list with a dictionary

my_odered_car = {
    'type' : 'standard four',
    'extras' : ['alloy wheels', 'climate control', 'leather seats']
}

# Print order summary
print("The car you ordered is a " + my_odered_car['type'] + " with the following extras:")

for extra in my_odered_car['extras']:
    print("\t" + extra)
