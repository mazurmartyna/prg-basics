# Write a program that calculates, prints, and saves to a text file 
# integers from 1 to 100 and their second and third powers. Sample result:


def f(file_name, result):
    with open(file_name, 'a') as file:
        file.write(f"{result}\n")
        

file_name= 'integers_exercise.txt'

x=0
y=0
z=0

for i in range(1,101):
    x= str(i)
    y= str(i*i)
    z= str(i*i*i)
    result = x +', '+ y +', ' + z 
    f(file_name, result )