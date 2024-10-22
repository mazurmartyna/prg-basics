
def triangle_area(a,b,c):
    obwpol= (1/2)*(a+b+c)
    result = (obwpol*(obwpol - a)*(obwpol - b)*(obwpol - c))**0.5
    return result

a = int(input('Triangle side a: '))
b = int(input('Triangle side b: '))
c = int(input("Triangle side c: "))

area = triangle_area(a,b,c)

print(f'The area of ​​a triangle with sides {a,b,c} is {area}')