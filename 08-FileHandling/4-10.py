import csv

with open('clothing.csv', 'r') as file:
    content = csv.reader(file)

    for row in content:
        if row[0] != 'Product_ID':
            x = float(row[5])
            if (x<60) and (int(row[6])<40):
                print(row)

