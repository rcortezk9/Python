# Creating our first class

class Books():
    """A class to create a book."""

    # Constructor
    def __init__(self, name, price, publisher):
        """Initialize the name, price, and publisher"""
        self.name = name
        self.price = price
        self.publisher = publisher

    def hardback(self):
        """Simulate a hard back book."""
        print(self.name.title() + " is a hardback book.")

    def softback(self):
        """Simulate being a softback"""
        print(self.name.title() + " is a softback book.")

    def ebook(self):
        """Simulate a ebook"""
        print(self.name.title() + " is an ebook.")

my_book = Books('elon musk', 14.99, 'virgin books')
