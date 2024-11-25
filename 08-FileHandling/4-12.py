import csv, re

def add_book(file_name, content):
    with open(file_name, 'a') as file:
        file.write(f"{content}\n")

        
with open('books.csv', 'r') as file1:
    text = csv.reader(file1)
    for row in text:
        if row[2] != 'Genre':
            genre = row[2]+'.txt'
            file_name= 'books_'+genre
            content = row[0] + ', ' + row[1] + ', ' + row[2] + ', ' + row[3]
            add_book(file_name, content)

