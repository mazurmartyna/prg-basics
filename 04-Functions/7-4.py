def letter(a,b):
    x=0
    a = a.casefold()
    for char in a:
        if char == b:
            x=x+1
    return x

if __name__ == "__main__":
    a = input('Write the sentence: ')
    b = input('What letter to count: ')
    print(f'The number of letter {b}: {letter(a,b)}')