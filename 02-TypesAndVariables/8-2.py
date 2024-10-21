###
# Calculation of circle area and circumference 
#

r = int(input('Radius: '))
pi = 3.141592

circumference = 2 * pi * r
circumference = round(circumference, 2)
area = pi * r**2
area = round(area, 2)

print(f'For radius: {r} the circumference is: {circumference}, the area is: {area}')