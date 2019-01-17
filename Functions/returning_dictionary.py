# Returning a dictionary

def build_book(name, author, publisher):
    book = {'name' : name, 'author' : author, 'publisher' : publisher}
    return book

my_book = build_book('elon musk', 'ashlee vanch', 'virgin boo')
print(my_book)
