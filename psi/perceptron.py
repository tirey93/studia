import numpy as np

def output(w1:float, x1:int, w2:float, x2:int, b:float):
    # return heavisade(w1*x1 + w2*x2 + b)
    return w1*x1 + w2*x2 + b

def output_matrix(w:np.array, x:np.array, b:float):
    # return heavisade(np.matmul(w, x.transpose()) + b)
    return np.matmul(w, x.transpose()) + b

def heavisade(x:float):
    if(x > 0):
        return 1
    else:
        return 0
    
# mamy punkty np 5 punktów
#i dodajemy wektor nauczyciela T i dla każdego punktu 1 oznacza nad osią, 0 pod osią