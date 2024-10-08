# d = 3.57 × √h
#d is the distance to the horizon in kilometers
#h is the height of the observer in meters

import math
h = input('Enter your height in cm: ')
h = int(h) / 100

d = 3.57 * math.sqrt(h)

print('Your distance from the horizon is:', d ,'when your hight is:', h, 'm') 