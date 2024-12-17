from functools import reduce

numbers = [2,4,6,3,7,5]

even_numbers = list(filter(lambda x:x%2==0,numbers))

add = lambda x,y: x+y

sum_e = reduce(add, even_numbers)

print(f"Sum of even numbers from {numbers} is {sum_e}")