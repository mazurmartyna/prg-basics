#Define the function f(number1,number2,number3), 
#which returns the difference between the largest 
#and smallest numbers. 


def f(number1,number2,number3):
    smallest = 0
    largest = 0
    if number1>number2:
        if number1>number3:
            largest=number1
            if number2>number3:
                smallest=number3
            else:
                smallest=number2
        else:
            largest=number3
            smallest=number2
    elif number1>number3:
        largest=number2
        smallest=number3
    else:
        smallest=number1
        if number2>number3:
            largest=number2
        else:
            largest=number3
        
    return largest -smallest

if __name__ == "__main__":
    print(f(2,12,8))


