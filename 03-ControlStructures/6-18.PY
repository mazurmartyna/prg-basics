x = int(input('Enter x: '))
y = int(input('Enter y: '))

if x==0:
    if y ==0:
        print(f'Point P({x},{y}) is in the position (0,0) of the coordinate system')
    elif y<0:
        print(f'Point P({x},{y}) is located on y-axis between the third and fourth quadrant of the coordinate system')
    else:
        print(f'Point P({x},{y}) is located on y-axis between the first and second quadrant of the coordinate system')
elif x<0:
    if y ==0:
        print(f'Point P({x},{y}) is located on x-axis between the second and third quadrant of the coordinate system')
    elif y<0:
        print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')
    else:
        print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')
else:
    if y ==0:
        print(f'Point P({x},{y}) is located on x-axis between the first and fourth quadrant of the coordinate system')
    elif y<0:
        print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system')
    else:
        print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')