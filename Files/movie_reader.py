# Read an entire file

# For absolute file path assign it to a variable
# file_path = '/Users/renemcortez/LearningPython/Files/movie_reader.py'
with open('movies.txt') as file_object:
    contents = file_object.read()
    print(contents.strip())
# if needing to open a file from different directory you would
# 'directory/file.txt'
