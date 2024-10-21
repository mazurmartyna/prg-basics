hours = int(input('The number of hours of parking: '))

if hours < 1:
    print('Parking free for one hour!')
elif hours >=1 and hours <=2:
    print('Parking fee: 5 PLN')
elif hours >=3 and hours <= 6:
    print('Parking fee: 15 PLN')
else:
    print('Parking fee: 20 PLN')