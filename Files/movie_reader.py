# Read an entire file

with open('movies.txt') as file_object:
    contents = file_object.read()
    print(contents.strip())
# if needing to open a file from different directory you would
# 'directory/file.txt'
