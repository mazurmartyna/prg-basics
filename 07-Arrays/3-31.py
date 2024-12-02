

def create_2d_arr(x,y):
    arrL = []
    for row in range(x):
        rowL = []
        for i in range(y):
            rowL.append("0")
        arrL.append(rowL)
    return arrL

print(create_2d_arr(3,5))