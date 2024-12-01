import codecs, re

with codecs.open('province.csv', 'r', 'utf-8') as file:
    provinces = file.read()

with open('vehicle.txt', 'r') as file:
    vehicles = file.read()


provinces = provinces.split()
provincesdict = {}

for item in provinces:
    provincesdict[item[0]]= item[2:(len(item))]

print(provincesdict)

total = 0
for dict in provincesdict:
    for item in vehicles:
        if item[0] == dict:
            total += 1
    print(f"{provincesdict[dict]} - {total}")
    total = 0