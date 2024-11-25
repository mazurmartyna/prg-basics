try:
    with open('it_company.csv', 'r') as file:
        content= file.read()
except FileNotFoundError:
    print(f"Hey! The file {'it_company.csv'} does not exist.")

for row in content:
    print(content[row[0]])

