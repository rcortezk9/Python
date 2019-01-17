# Passing a list to a function

def books_available(books):
    for book in books:
        books_in_stock = "The following title is available to buy " + book.title() + "."
        print(books_in_stock)

available = ['elon musk', 'the everything store', 'the growth map']
books_available(available)
