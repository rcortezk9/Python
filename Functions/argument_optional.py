# Making arguments optional

# Since the middle name is going to be optional you want to move
# that parameter to the end and assigning an empty string
def formatted_name(first_name, last_name, middle_name=''):

    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

# If you are to use it as an option you can enter the middle name
# as the last argument
teacher = formatted_name('rene', 'cortez', 'morales')
print(teacher)

# Optional middle name 
teacher = formatted_name('rene', 'cortez')
print(teacher)
