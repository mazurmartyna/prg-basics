tuple = (10,20,30,40,50)
art = []
i=0

for i in range(len(tuple)):
    art.append(tuple[len(tuple)-(i+1)])

print(art)