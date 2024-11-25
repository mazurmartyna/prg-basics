import csv

csv_file = 'it_company.csv'

with open(csv_file, 'r') as file:
    reader = csv.reader(file)

    print("GRAPHIC DESIGNERS")
    print("=================")

    for row in reader:
        for item in row:
            if item == 'Graphic Designer':
                print(row[1], row[0], end=', ')
                print(row[3])