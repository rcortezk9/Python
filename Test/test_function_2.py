# Testing a function

from test_function_1 import get_formatied_name

print("Enter 'q' to quit this program.")
while True:
    first = input("\nPlease enter your first name: ")
    if first == 'q':
        break

    last = input("\nPlease enter your last name: ")
    if last == 'q':
        break

    formatted_name = get_formatied_name(first, last)
    print("Your name is " + formatted_name + ".")
