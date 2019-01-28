# Writting to an empty file

# filename = 'programming.txt'
#
# with open(filename, 'w') as file_object:
#     file_object.write("Hello, my name is Rene.")

# Writing multiple lines to a file and using the append

message = input("What is your favorit file?")
print(message.title())

filename = 'favorit_file.txt'

with open(filename, 'a') as file_object:
    file_object.write(message + "\n")
