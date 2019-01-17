# Using positional and arbitary arguments together

def assign_seat(seat, *requests):
    """Assign a seat and request to a passenger"""
    print("\nPassenger is assigned to seat number " + str(seat) + " with the following request:")
    for request in requests:
        print("- " + request)

assign_seat(36, 'window seat')

# Output:

# Passenger is assigned to seat number 36 with the following request:
# - window seat
