# Analyzing Text
# Working with multiple files
def word_count(filename):
    """count the number of words in a file"""

    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
        # message = "Sorry, the file " + filename + " cannot be found"
        # print(message)
    else:
        words = contents.split()
        number_words = len(words)
        print('The file ' + filename + " has approximately " + str(number_words) + " words")

# Assign file names to be anaylze to a variable
filenames = ['heathcliff.txt', 'mobydick.txt']
for filename in filenames:
    word_count(filename)
