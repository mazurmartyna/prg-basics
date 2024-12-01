import json

# Open the JSON file in read mode

with open('computer.json', 'r', encoding='utf-8') as file:
   data = json.load(file)   # Load the data from the JSON file into a variable

# Print the JSON data
for item , value in data.items():
   print(item,':',value)