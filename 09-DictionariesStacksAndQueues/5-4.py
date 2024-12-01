winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}

total = 0
for dict in winter_semester:
    total += winter_semester[dict]

print(f"The total number of hours in the winter semester is ", total)