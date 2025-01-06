classification = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]

countries = list(map(lambda x: x["country"], classification))

add = lambda x: x["gold"] + x["silver"] + x["bronze"]
total_medals= list(map(add, classification))

print(total_medals) 

print("Total number of medals won by each country")
print("__________________________________________\n\n")
print("(Countries)")
x=0
for item in countries:
    print(f"{item:10} |", end=' ')
    
    
    for i in range(total_medals[x]):
        print("=", end='')
    print('')
    x+=1

print(f"{' ':10}   1   5  8 10   15   20  25 28  (Number of medals won)")

