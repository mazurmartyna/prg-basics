def f(detector):
    x=0
    for char in detector:
        if char == '+':
            x=x+1
        else:
            x = x-1
        if x==3:
            break
    if x==3:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f("++-+----+"))