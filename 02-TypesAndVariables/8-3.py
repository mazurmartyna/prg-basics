#Temperature converter
celsius = int(input('Temperature in celsius: '))

#Converting celsius to kelvin
kelvin = celsius + 273.15

#Converting celsius to fahrenheit
fahrenheit = celsius * 9 / 5 + 32

print(f'Temperature in kelvin: {kelvin} \nTemperature in fahrenheit: {fahrenheit}')
