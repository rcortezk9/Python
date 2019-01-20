# Creating a new ereader class

class Ereader():
    """A class to represent an ereader."""

    def __init__(self, make, model, backlight, battery, screen_type):
        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery = battery
        self.screen_type = screen_type

    def get_ereader_name(self):
        long_name = self.make + ' - ' + self.model + ' - ' + self.backlight + ' - ' + self.battery + ' - ' + self.screen_type

        return long_name.title()

my_new_erearder = Ereader('Amazon Kindle', 'Paperwhite', 'Adjustable', 'Several month of battery life', '300 DPI')

print(my_new_erearder.get_ereader_name())
