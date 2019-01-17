# Default Values

# create a function
def book_description(author_name, book_type="non-fiction"):
    """display book information"""

    print("\nThis is a " + book_type + " book.")
    print("The author of this book is " + author_name.title() + ".")

# We don't have to enter the book type argument because the value was define as part of the pramaters
book_description('ashlee vance')
