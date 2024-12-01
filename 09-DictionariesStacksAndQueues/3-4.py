import queue

binary = queue.LifoQueue()

number = int(input("Type in a natural number: "))
remainder = 0
binaryNumber = ''
naturalnumber = number

while number != 0:
    remainder = number % 2
    number = number // 2
    binary.put(remainder)

while binary.qsize() > 0:
    binaryNumber += str(binary.get()) 


print(f"Natural number: ", naturalnumber)
print(f"Binary number: ", binaryNumber)


