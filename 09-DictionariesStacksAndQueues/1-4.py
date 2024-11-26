person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

#1.
print(person['name'])

#2.
for item in person['hobby']:
    print(item, end=', ')
print()


#4.
person["surname"] = 'Nowak'

#5.
person["married"] = False

#6.
person["gender"] = 'male'

#7.
person["hobby"] += {'bicycle'}

#8.

for dict in person:
        dict["phone"] += {"work phone":'313131444'}
        
        
#3.
for item,value in person.items():
    print(f"{item}: {value}")