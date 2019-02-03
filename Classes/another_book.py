# Creating a new ereader class
# Setting a default value for an attribute
# Modifying an attributes value directly
# Modifying an attribute value through a method
# Incrementing an attributes value through a method.

class Ereader():
    """A class to represent an ereader."""

    def __init__(self, make, model, backlight, battery, screen_type):
        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery = battery
        self.screen_type = screen_type
        self.library_count = 0

    def get_ereader_name(self):
        long_name = self.make + ' - ' + self.model + ' - ' + self.backlight + ' - ' + self.battery + ' - ' + self.screen_type

        return long_name.title()

    def read_library_count(self):
        print("You have " + str(self.library_count) + " books in your kindle library.")

    def update_library_count(self, ebook_count):
        self.library_count = ebook_count

    def increment_library_count(self, purchased_ebooks):
        self.library_count += purchased_ebooks

my_new_erearder = Ereader('Amazon Kindle', 'Paperwhite', 'Adjustable', 'Several month of battery life', '300 DPI')
print(my_new_erearder.get_ereader_name())

my_new_erearder.update_library_count(48)
my_new_erearder.read_library_count()

my_new_erearder.increment_library_count(5)
my_new_erearder.read_library_count()
