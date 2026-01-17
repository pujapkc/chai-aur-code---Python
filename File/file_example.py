# file = open("File/my_file.txt")

# contents = file.read()

# print(contents)

# file.close()

with open("File/my_file.txt", mode = "a") as file:
    file.write("new text")