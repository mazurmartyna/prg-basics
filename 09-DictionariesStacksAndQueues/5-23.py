import json

with open('euro.json', 'r') as file:
    content = json.load(file)


print("Date            Buying Rate     Selling Rate")
print("============================================")

for item in content['rates']:
    print(item['effectiveDate'], end='      ')
    print(item['bid'], end='          ')
    print(item['ask'])
    