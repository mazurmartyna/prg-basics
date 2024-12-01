import json

with open('reservations.json', 'r', encoding= 'utf-8') as file:
    data = json.load(file)

def numbrooms(hotel):
    result = 0
    for item in hotel['reservations']:
        result += 1
    return result

def numbpres(hotel):
    result = 0
    for item in hotel['reservations']:
        if item['paid'] == True:
            result = result + 1
    return result

def numbupres(hotel):
    result = 0
    for item in hotel['reservations']:
        if item['paid'] == False:
            result = result + 1
    return result

def totalpaid(hotel):
    result = 0
    for item in hotel['reservations']:
        if item['paid'] == True:
            result = result + item['nights'] * item['price_per_night']
    return result

def totalunpaid(hotel):
    result = 0
    for item in hotel['reservations']:
        if item['paid'] == False:
            result = result + item['nights'] * item['price_per_night']
    return result

print("number of rooms: ", numbrooms(data))
print("number of paid reservations: ", numbpres(data) )
print("number of unpaid reservations: ", numbupres(data))
print("total value of paid reservations", totalpaid(data))
print("total value of unpaid reservations", totalunpaid(data))
