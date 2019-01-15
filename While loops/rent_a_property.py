# Adding user input to a dictionary

# Create an empty dictionary
rental_properties = {}

# Set a flag to indicate we taking applictaions
rental_open = True

while rental_open:
    # Prompt users for users name and addressself.
    username = input("\nWhat is your name? ")
    rental_property = input("What is the address of the property? ")

    # Store the responses in a dictionary
    # rental_properties = {
    #    username: rental_property
    #}
    rental_properties[username] = rental_property

    # Ask if the user knows anyone else looking to rent a property
    repeat = input("\nDo you know anyone who might like to rent out their property? ")
    if repeat == 'no':
        rental_open = False

# Adding property is complete
print("\n--- Propert to rent ---")
for username, rental_property in rental_properties.items():
    print(username + " has " + rental_property + " to rent. ")
