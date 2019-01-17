# Making arguments optional

def formatted_name(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

teacher = formatted_name('rene', 'morales', 'cortez')
print(teacher)
