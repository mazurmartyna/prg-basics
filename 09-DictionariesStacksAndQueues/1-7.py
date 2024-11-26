store = {
   'Laptop': 15,
   'Desktop PC': 10,
   'Monitor': 25,
   'Keyboard': 50,
   'Mouse': 60,
   'External Hard Drive': 30,
   'Printer': 12,
   'Router': 20,
   'USB Flash Drive': 100,
   'Graphics Card': 8
   }

for item,value in store.items():
    print(f"{item}: {value}")

total = 0
for count in store.values():
    total += count

print(f"Total number of product in store: {total}")