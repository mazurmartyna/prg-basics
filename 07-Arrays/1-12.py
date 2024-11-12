categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

i=0
for i in range(len(expenses)):
    if expenses[i] == max(expenses):
        print('The most expensive category is:', categories[i])