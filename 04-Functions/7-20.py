def f(n):
    prime = True
    
    i=1
    x=0
    while x<n:
        i=i+1
        for a in range(2,i):
            if (i%a ==0) and (i!=a):
                prime = False
                break
            else:
                prime = True
        if prime == True:
            x=x+1
    
    return i


if __name__ == "__main__":
    print(f(5))
            