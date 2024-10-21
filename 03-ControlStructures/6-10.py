dog_age = int(input('Enter the dogs age in human years:  '))
dog_years = 0
if dog_age<=2:
    dog_years= dog_age*10.5
else:
    dog_years=2*10.5 + (dog_age-2)*4

print(f'The dogs age in dogs years is: {dog_years} years.') 