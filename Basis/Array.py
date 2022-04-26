import numpy as np
import fractions

def tabulate(func, hi, low = 0):
    '''
    Tabulates a new vector using a given function.
    
    param func <function object> : A function from int -> Any.
    param hi int: Highest index
    param low int (default = 0): Lowest index
    
    '''
    return np.vectorize(func)(np.arange(low, hi))

def matrix_tabulate(func, shape):
    '''
    Tabulates a new matrix using a given function.
    
    param func <function object> : A function from (int, int) -> Any.
    param shape Tuple(int, 2): shape of the desired output
    
    '''
    m, n = shape
    indices = np.arange(m*n).reshape(m, n)
    return np.vectorize(lambda i: func(i % m, int((i - i%m)/m)))(indices)


def Fraction(M, max_denom = 100):
    return np.vectorize(lambda s: fractions.Fraction(s).limit_denominator(max_denom))(M)