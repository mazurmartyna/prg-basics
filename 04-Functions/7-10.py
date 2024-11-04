def f(x,y):
    a=0
    for i in range (x,y):
        if i<0:
            if i%2 ==0:
                a=a+1
    return a

if __name__ == "__main__":
    x= -9
    y= 22
    print(f'f({x},{y}) returns {f(x,y)}')