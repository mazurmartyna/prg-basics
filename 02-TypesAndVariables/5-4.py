print('Type in the amount:')
a= input('amount=')
a= float(a)
vat=a*23/100
vat = round(vat,2)
print(f'Amount  :  {a}')
print(f'VAT 23% :  {vat}')
