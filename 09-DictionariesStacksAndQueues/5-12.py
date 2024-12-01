import queue

def reverse(text):
    result=''
    stack = queue.LifoQueue()
    
    for char in text:
        stack.put(char)
    while not stack.empty():
        result += stack.get()
    return result

text = input("Enter text: ")

print("Reversed text: ", reverse(text))