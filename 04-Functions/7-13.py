def f(n):
    x=''
    for i in range(1,n+1):
        i= str(i)
        x= x+i
    return x

if __name__ == "__main__":
    print(f(4))