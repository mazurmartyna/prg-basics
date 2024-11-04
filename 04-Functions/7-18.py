def f(sentence):
    x=''
    for char in sentence:
        if char != ' ':
            x=x+char
    return x

if __name__ == "__main__":
    print(f("Ala ma kota"))