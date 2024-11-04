def f(number):
    x=0
    number = str(number)
    count = 0

    for i in range(0,10):
        for char in number:
            numb = int(char)

            if (i == numb):
                count = count +1
           
        if count >1:
            x = x+i*count
        count = 0

    return x

if __name__ == "__main__":
    print(f(513553007))