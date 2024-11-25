employees_file = 'it_company.csv'

with open(employees_file, 'r') as file:
    content= file.read()

file_lines = content.splitlines()

i=0

for line in file_lines:
    if i==5:
        press = input('Press enter key...')
        i=0
    print(line)
    i= i+1

   