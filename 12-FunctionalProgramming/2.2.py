names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

argument = lambda names: len(names)

sorted_list = sorted(names, key=argument)

print(f"Sorted list: {sorted_list} ")