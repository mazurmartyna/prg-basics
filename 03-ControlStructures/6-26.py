pin = '0805'


for i in range(3):
    enter_pin = input('Enter the pin code: ')
    if enter_pin == pin:
        print('Correct pin!')
        break
    else:
        print('Incorrect')

if enter_pin != pin:
    print('Sorry, your payment card has been blocked')

