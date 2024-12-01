basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}

person = {}

for dict in basic_data:
    person[dict] = basic_data[dict]

for dict in advanced_data:
    person[dict] = advanced_data[dict]

print (person)