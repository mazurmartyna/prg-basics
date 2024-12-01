import json

json_file = open('voting.json', 'r', encoding='utf-8')
file = json.load(json_file)
json_file.close()


# Vote for a person
person_name = input('Name of the person you are voting for:')

if person_name in file:
    total = file[person_name] + 1
else:
    total = 1


file[person_name] = total
total = 0

json_file = open('voting.json', 'w', encoding='utf-8')
json.dump(file, json_file, ensure_ascii=False)
json_file.close()