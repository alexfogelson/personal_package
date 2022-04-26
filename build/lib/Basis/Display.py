import numpy as np
import fractions
from Array import matrix_tabulate

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
