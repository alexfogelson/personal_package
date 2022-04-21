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

def zero_print(X, precision = 2, **kwargs):
    '''
    Prints X as nicely formatted where elements close to zero are printed as "0"
    
    param X np.ndarray : Input matrix
    param precision int (default 2) : Rounding precision
    param atol, rtol float : Passed into np.isclose.
    
    '''
    
    assert len(X.shape) <= 2, "Currently printing higher dimensional arrays is not supported."

    row_array = []

    for row in X:
        element_array = []
        for element in row:
            if (np.isclose(element, 0, **kwargs)):
                element_array.append("0")
            else:
                element_array.append(str(round(element, precision)))
        row_array.append(element_array)
    
    greatest_length = matrix_tabulate(lambda i,j: len(row_array[i][j]), X.shape).max()

    row_array_padded = [[element + (greatest_length - len(element))*" " for element in row] for row in row_array]

    final_output = "\n".join([" ".join(row) for row in row_array_padded])

    print(final_output)

def get_batches(X, Y, batch_size):
    indices = np.random.permutation(len(X))

    while (len(indices) > 0):
        yield X[indices[:batch_size]], Y[indices[:batch_size]]
        indices = indices[batch_size:]

def Fraction(M, max_denom = 100):
    return np.vectorize(lambda s: fractions.Fraction(s).limit_denominator(max_denom))(M)
