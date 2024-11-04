import keyboard


first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter last name:')
age = keyboard.input_integer('Enter your age')
salary = keyboard.input_integer("Enter your salary: ")
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Last name: ', last_name)
print('Age: ', age)
if is_salary_hidden == False:
    print('Salary: ', salary)