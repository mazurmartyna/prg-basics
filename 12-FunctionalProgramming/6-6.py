arr = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

capital = lambda x: x.upper()

listcap = list(map(lambda x: capital(x[0]) +', '+x[1],arr ))

print(listcap)

