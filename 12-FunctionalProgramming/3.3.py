stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]


result1= sum(list(map(lambda x: x[0]*x[1],stock)))

count = lambda x: x[0]*x[1]
result= sum(list(map(count,stock)))


print("Total value:", result)