def f(n1,n2,n3):
    if (n1<0) or (n2<0) or (n3<0):
        return True
    else:
        return False
    
if __name__ == "__main__":
    n1= int(input('n1 = '))
    n2 = int(input('n2 = '))
    n3 = int(input('n3 = '))
    print(f'f({n1,n2,n3}) returns {f(n1,n2,n3)}')