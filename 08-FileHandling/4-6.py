file_name = input("Type in the full name of the file: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"Hey! The file {file_name} does not exist.")

content_lines = content.splitlines()
content_items = content.split()

numberoflines = 0
numberofwords = 0
numberofcharacters = 0


for item in content_items:
    numberofwords = numberofwords + 1

for line in content_lines:
    numberoflines = numberoflines + 1
    for char in line:
            numberofcharacters = numberofcharacters + 1


print("File name: ", file_name)
print("Number of lines: ", numberoflines)
print("Number of characters: ", numberofcharacters)
print("Number of words: ", numberofwords)