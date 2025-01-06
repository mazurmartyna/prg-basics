temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

result = list(filter(lambda x:temp[x]>=0 ,temp))

answer = ''
for item in result:
    answer = answer+ item +' ' 

print("Cities with positive temperatures:", answer)