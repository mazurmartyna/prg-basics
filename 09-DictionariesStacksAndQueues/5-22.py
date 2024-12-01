import json

product = {}

name = input("Enter name: ")
price = float(input("Enter price (real number with two decimal places): "))
ispaid = input("Is it paid: yes/no ")

if ispaid == 'yes':
    paid = True
else:
    paid = False

product['name'] = name
product['price'] = price
product['ispaid'] = paid

file_name = 'product.json'

with open(file_name, 'w') as file:
    json.dump(product, file, indent=4)

print("Data has been printed to: ", file_name)