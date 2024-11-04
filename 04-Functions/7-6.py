def hide(card_number):
    card_number = str(card_number)
    x = ''
    x = card_number[0] + card_number[1]
    for i in range(0,10):
        x = x + '*'
    for char in card_number[12:16]:
        x = x + char
    return x

if __name__ == "__main__":
    card_number = 5290312400019022
    print(card_number)
    print(hide(card_number))