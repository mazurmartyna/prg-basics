###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
#
age = int(input('Enter your age: '))

if age < 18 or age >= 65 :
    print(f'age {age} is eligible for the discount')
else:
    print(f'age {age} is not eligible for the discount')