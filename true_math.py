import math as mat
def divide(first, second):
    if second == 0:
        return mat.inf
    else:
        res = int(first) / int(second)
        return res