import queue

expression = input("Enter expression: ")

total = 0
stack = queue.LifoQueue()

for char in expression:

    if char != ' ' and char != '-' and char != '*' and char != '/' and char != '=' and char != '+':
        char= int(char)
        stack.put(char)
    elif char == '+':
        total = int(stack.get())
        total = total + int(stack.get())
        stack.put(total)
        
    elif char == '-':
        total = int(stack.get())
        total = int(stack.get()) - total
        stack.put(total)
        
    elif char == '*': 
        total = int(stack.get())
        total = total * int(stack.get())
        stack.put(total)
        
    elif char == '/': 
        total = int(stack.get())
        total = int(stack.get()) / total
        stack.put(total)
       
    elif char == '=':
        result = int(stack.get())
        print("The result is: ", result)


    
