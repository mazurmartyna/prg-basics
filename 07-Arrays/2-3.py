# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements

food = 0
transport = 0
utilities = 0

week_1 = 0
week_2 = 0
week_3 = 0
week_4 = 0

i=0
for row in monthly_expenses:
    food = food + monthly_expenses[i][0]
    transport = transport + monthly_expenses[i][1]
    utilities= utilities + monthly_expenses[i][2]
    i=i+1

for item in monthly_expenses[0]:
    week_1 = week_1 + item

for item in monthly_expenses[1]:
    week_2 = week_2 + item

for item in monthly_expenses[2]:
    week_3 = week_3 + item    

for item in monthly_expenses[3]:
    week_4 = week_4 + item

total = week_1 + week_2 + week_3 + week_4
# Print expenses

print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food)
print('Transport:', transport)
print('Utilities:', utilities)
print('Week 1:', week_1)
print('Week 2:', week_2)
print('Week 3:', week_3)
print('Week 4:', week_4)
print('---------------')
print('TOTAL:', total)