import queue



expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct


def brackets_ok(expression):
    brackets = queue.LifoQueue()
    bracket = ''  
    for char in expression:
        if char == "[" or char == "(" or char == "{":
            brackets.put(char)
        elif char == "]" or char == ")" or char == "}":
            bracket = brackets.get()
            
            if bracket == "[":
                if char == "]":
                    result = True
                else:
                    return False
            elif bracket == "(" :
                if char == ")":
                    result= True
                else:
                    return  False    
            else:
                if char == "}":
                    result = True
                else:
                    return  False  
    i = brackets.qsize()
    if i != 0:
        result = False
        bracket =''

    return result
                    

if brackets_ok(expression1):
   print("The brackets are used correctly in expression: ", expression1)
else:
   print("The brackets are NOT used correctly in expression: ", expression1)

if brackets_ok(expression2):
    print("The brackets are used correctly in expression: ", expression2)
else:
   print("The brackets are NOT used correctly in expression: ", expression2)

if brackets_ok(expression3):
    print("The brackets are used correctly in expression: ", expression3)
else:
   print("The brackets are NOT used correctly in expression: ", expression3)