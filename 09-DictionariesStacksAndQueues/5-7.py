hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

total= 0


def hotel_list(hotels):
    result = ''
    for item in hotels:
        result +=  item['name'] + ','
    return result

def avg_price(hotels):
    total= 0
    for item in hotels:
        total = total + item['price']
    return round(total)

print("Hotels in Krakow: ", hotel_list(hotels_in_Krakow))
print("Average hotel price in Krakow: ", avg_price(hotels_in_Krakow))
print("Hotels in Sopot: ", hotel_list(hotels_in_Sopot))
print("Average hotel price in Sopot: ", avg_price(hotels_in_Sopot))

if avg_price(hotels_in_Krakow) < avg_price(hotels_in_Sopot):
    cheaper = "Krakow"
else:
    cheaper = "Sopot"

print("Cheaper hotels in: ", cheaper)
