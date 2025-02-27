import numpy as np

def output(w, x, b:float):
    res = test(w,x,b)
    # print(f"res: {res} for x: {x}")
    return heavisade(res)

def test(w, x, b:float):
    return np.matmul(w, x.transpose()) + b
def heavisade(x:float):
    if(x > 0):
        return 1
    else:
        return 0
    
def mean_squared_error(y_true, y_predicted):
    return np.mean((y_predicted - y_true) ** 2)