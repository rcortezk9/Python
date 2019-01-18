# Importing a module

from books_to_buy import books_available, book_description # Import just a function
# To use alias you would put in "as ba" short version of one of the other function

print("This is our first functions: ")
books_available('Elon Musk')

print("This is our 2nd function: ")
book_description('ashlee vance')
# For alias this would change to ba('ashlee vance')

# Output

# This is our first functions:
# The following title is available to buy Elon Musk
# This is our 2nd function:
#
# This is a non-fiction book.
# Then author of this book is Ashlee Vance.
