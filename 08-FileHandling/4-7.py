import re

text = input("Enter text: ")

pattern = '[a,e,i,o,u,y,A,E,I,O,U,Y]'

vowels = re.findall(pattern,text)

i=0
for item in vowels:
    i += 1

print("The number of vowels is: ",i)