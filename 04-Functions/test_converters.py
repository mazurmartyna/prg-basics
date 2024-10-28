import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
y= converters.m_to_cm(3)
print(f'{y}cm is {round(converters.cm_to_inch(y),2)} inches')
x=converters.cm_to_inch(converters.m_to_cm(3))
x= round(x,2)
print(f'{x} inches is {converters.feet_inch_to_cm(0,x)} cm')

