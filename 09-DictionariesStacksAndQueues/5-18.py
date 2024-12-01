import json

with open('dogs.json', 'r', encoding='utf-8')as file:
    data= json.load(file)

for name in data:
    if int(name['age']) < 5:
        for key, value in name.items():
            print(key,':',value)
        print()