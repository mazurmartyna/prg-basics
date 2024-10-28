x=0
y=1

print(x,y,end=' ')
for i in range(18):
    z = x+y
    x= y
    y= z
    print(z, end=' ')