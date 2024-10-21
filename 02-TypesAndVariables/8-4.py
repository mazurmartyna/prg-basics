###
# A program that prints your height both in cm 
# and in feet and inches.
#
cm = 170
feet =  0.0328 * cm
inches = cm *  0.393701
# calculate the number of feet
n_feet = inches // 12
n_inches = round(feet % 1, 2)
print(f'I am {cm}cm tall, i.e. {n_feet} feet and {n_inches} inches')