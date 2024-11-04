def rangecheck(n,x,y):
    if (n>=x) and (n<=y):
        return True
    else:
        return False
    
if __name__ == "__main__":
    n= int(input('Enter a number: '))
    x = int(input('Enter beginning of range: '))
    y= int(input('Enter the end of range: '))
    print(f'Number {x} in the range <{x},{y}>: {rangecheck(n,x,y)} ')