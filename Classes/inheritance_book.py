# Storing multiple models.

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


class Screen():
    """Create a class to model the screen of a kindle fire"""
    def __init__(self, screen_resolution='1280 * 800'):
        """Initialize the screens attributes."""
        self.screen_resolution = screen_resolution

    def describe_screen(self):
        print("\nFire HD 8 feature a widescreen " + self.screen_resolution + " HD screen.")

class KindleFire(Ereader):

    def __init__(self, make, model, backlight, battery, screen_type,):

        super().__init__(make, model, backlight, battery, screen_type)
        self.firescreen = Screen() # Create an new instance of screen. Store that in attribute
