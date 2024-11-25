import re

pattern = '(\S+\.\w{4})'

file_name = 'files.txt'

with open(file_name, 'r') as file:
    content = file.read()

result = re.findall(pattern, content)

print(result)