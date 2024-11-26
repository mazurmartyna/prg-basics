price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}


#prints a list of products and their prices before the discount

for item,value in price_list.items():
    print(f'{item}: {value}')

total_before = 0
for count in price_list.values():
    total_before += count
    total_before = round(total_before,2)

print(f"Total value of products before discount: {total_before} ")

updated = {}

for item, value in price_list.items():
    value = 0.9* value
    value = round(value,2)
    updated[item] = value


for item, value in updated.items():
    print(f'{item}: {value}')

total_after = 0
for count in updated.values():
    total_after += count
    total_after = round(total_after,2)

print(f"Total value of products after discount: {total_after}")
