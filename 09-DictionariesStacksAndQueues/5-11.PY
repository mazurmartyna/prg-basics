import json

json_file = open('voting.json', 'r', encoding='utf-8')
file = json_file
json_file.close()

content = {}

# Vote for a person
person_name = input('Name of the person you are voting for:')

content[person_name] = 1

# Save voting data to json file

json_file = open('voting.json', 'a', encoding='utf-8')
json.dump(content, json_file, ensure_ascii=False)
json_file.close()