# Passing information to a function

def hello_world(username):
    """showing a username"""
    print(" Hello " + username.title() + ".")

# We pass the argument Rene into the function
hello_world('rene')

# Positional argument
# Creating our function
def book_description(book_type, author_name):
    print("\nThis Book is " + book_type + ".")
    print("The author of this book is " + author_name.title() + ".")

book_description('non-fiction', 'ashlee vance')
book_description('fiction', 'dan brown')
