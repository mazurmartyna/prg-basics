def month(n):
    if n==1:
        return 'Jenuary'
    elif n==2:
        return 'February'
    elif n==3:
        return 'March'
    elif n==4:
        return 'April'
    elif n==5:
        return 'May'
    elif n==6:
        return 'June'
    elif n==7:
        return 'July'
    elif n==8:
        return 'August'
    elif n==9:
        return 'September'
    elif n==10:
        return 'October'
    elif n==11:
        return 'November'
    else:
        return 'December'
    
if __name__ == "__main__":
    n = int(input('Enter month number: '))
    print(f'The name of month {n} is {month(n)}')