def f(n):
    x=''
    if n>0:
        x = '*'
    for i in range(1,n):
        x = x +'/*'
    return x


if __name__ == "__main__":
    print(f(2))