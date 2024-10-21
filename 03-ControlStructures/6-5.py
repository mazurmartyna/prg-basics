temperature = int(input('Type in the temperature: '))

if temperature > 35:
    print(f'It is extremaly hot! {temperature}*C')
elif temperature <= 35 and temperature > 30:
    print(f'It is hot. {temperature}*C')
elif temperature <= 30 and temperature >= 15:
    print(f'It is warm. {temperature}*C')
elif temperature < 15 and temperature >= 0:
    print(f'It is cold. {temperature}*C')
else:
    print(f'Warning! Frost! {temperature}*C')