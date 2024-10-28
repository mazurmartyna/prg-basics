ean = input('Enter EAN-13 article number: ')

if len(ean) == 13:
    print('Article number is correct')
    if (ean[0] == '5') and (ean[1] == '9') and (ean[2] == '0'):
        print('Article is from Poland')
else:
    print('Article number is incorrect')