# Creating a list of numbers
# Coverting number into a list
numbers = list(range(1,6))
print(numbers)

odd_number = list(range(1,101,2))
print(odd_number)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = [1,2,3,4,5]
print(max(digits))
