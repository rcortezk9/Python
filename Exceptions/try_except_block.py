# Using the try-exception block

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
#
# print("Please enter another number.")

# The else block
print("Please enter two numbers to be divided")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break

    second_number = input("Second Number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0.")
    else:
        print(answer)
