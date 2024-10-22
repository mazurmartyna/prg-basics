


def sum_digits(number):
    sum = 0
    number= abs(number)
    number = str(number)
    for char in number:
        liczba = int(char)
        sum = sum + liczba
    return sum

any_number = int(input('Enter integer number: '))

result = sum_digits(any_number)

print(f'The sum of the digits in the number {any_number} is {result}')
