print('N leading prime numbers ')
n = int(input('Enter the N '))
prime = True
for i in range (2,n):
    for a in range(2,i):
        if (i%a == 0) and (i!=a):
            prime = False
            break
        else:
            prime= True
    
    if prime == True:

        print(i, end=' ')