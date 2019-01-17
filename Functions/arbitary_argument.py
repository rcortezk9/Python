# Arbitary arguments

# In the function definition we use an asterisk (*)
# before the parameter name to denote this kind of argument.
def create_passenger(*requests):
    """Summarize passenger request"""
    for request in requests:
        print("-" + request)

create_passenger('window seat', 'seat near top of the plan', 'pre-order breakfast')


# output :

# -window seat
# -seat near top of the plan
# -pre-order breakfast
