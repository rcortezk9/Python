# Arbitary arguments

# In the function definition we use an asterisk (*)
# before the parameter name to denote this kind of argument.
def create_passenger(*request):
    """Print user requests"""
    print(request)

create_passenger('window sea', 'seat near top of the plan', 'pre-order breakfast')
