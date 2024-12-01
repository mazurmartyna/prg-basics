import queue

customerqueue = queue.Queue()

customerqueue.put(1)
customerqueue.put(2)
customerqueue.put(3)


print("1 -- New customer")
print("0 -- Close ")

choice = 1
i=3

while choice != 0:
    choice = input("Enter 1 or 0: ")
    i += 1
    customerqueue.put(i)
    customer = customerqueue.get()
    print(f"Customer {customer} is served")
