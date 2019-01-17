# Modifying a list in a function

def passengers(not_checked_in, checked_in):
    """Simulate passengers who are not checked in"""
    while not_checked_in:
        current_passenger = not_checked_in.pop() # remove last item on the list

        # Simulate checking a passenger inself.
        print("Checking in passenger: " + current_passenger)
        checked_in.append(current_passenger) # Add to the check in list

def show_checked_in_passengers(checked_in):
    """Show all the passengers who have checked in."""
    print("\nThe following passengers have been checked in: ")
    for passengers in checked_in:
        print(passengers)

not_checked_in = ["Rene Cortez", "Stephanie Cortez", "Mariah Cortez"] # Assigning person to not checked in list
checked_in = [] # Left blank because we are going to move the to this list


passengers(not_checked_in, checked_in)
show_checked_in_passengers(checked_in)
