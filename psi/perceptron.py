import numpy as np

def output(w:np.array, x:np.array, b:float):
    return np.matmul(w, x.transpose()) + b

def heavisade(x:float):
    if(x > 0):
        return 1
    else:
        return 0