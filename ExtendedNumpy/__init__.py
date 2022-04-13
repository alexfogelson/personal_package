import numpy as np

def tabulate(func, hi, low = 0):
    '''
    Tabulates a new vector using a given function.
    
    param func <function object> : A function from int -> Any.
    param hi int: Highest index
    param low int (default = 0): Lowest index
    
    '''
    return np.vectorize(func)(np.arange(low, hi))
