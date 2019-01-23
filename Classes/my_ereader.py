import inheritance_book

my_kindle_fire = inheritance_book.KindleFire('amazon', 'kindle fire', 'color screen', '12 hour battery life', '1280 * 300')
print(my_kindle_fire.get_ereader_name())

print(my_kindle_fire.firescreen.describe_screen())

my_bw_reader = inheritance_book.Ereader('amazon', 'paperweight', 'adjustable backlight', 'several month of battery life', '300 dpi')
print(my_bw_reader.get_ereader_name())

my_color_ereader = inheritance_book.KindleFire('amazon', 'kindle fire', 'color screen', '12 hours of battery life', '1280 * 800')
print(my_color_ereader.get_ereader_name())
