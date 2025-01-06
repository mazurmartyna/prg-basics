bottles = [508,500,512,499,492,511,503,476,501,509]

def tolerance(x,cap,tol):
    diff = round(cap*tol/100)
    if (x >= (cap-diff)) and (x<= (cap+diff)):
        return x

capacity = 500
tol_p = 2
correct_bottles = list(filter(lambda x: tolerance(x,capacity,tol_p), bottles))


incorrect = 100 - round(len(correct_bottles)/len(bottles)*100)

print(f"{"Bottle capacity:":20} {capacity}ml")
print(f"{"Filling tolerance:":20} 2%")
print(f"{"Filled bottles:":20} {bottles}")
print(f"{"Incorrectly filled:":20} {incorrect}%")
