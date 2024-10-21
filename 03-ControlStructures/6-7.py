age = int(input('Please type in your age: '))

if age<13:
    print("Your age group is: Child")
elif age>=13 and age <= 19:
    print("Your age group is: Teen")
elif age>=20 and age <= 64:
    print("Your age group is: Adult")
else:
    print("Your age group is: Senior")