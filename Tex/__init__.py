import numpy as np


def format_element_(x, precision = 2, **kwargs):
    if (np.isclose(x, 0, **kwargs)):
        return "0"
    else:
        return str(round(x, precision))

def NumpyToTex(M, precision = 2, **kwargs):
    '''
    Prints M nicely to be pasted directly into LaTeX.
    
    param M np.ndarray : Input matrix
    param precision int (default 2) : Rounding precision
    param atol, rtol float : Passed into np.isclose.
    
    '''
    assert len(M.shape) <= 2, "Cannot convert ndarray of dimensionality > 2 into LaTeX."

    row_array = [[format_element_(element, precision = precision, **kwargs) for element in row] for row in M]

    matrix_interior = " \\\\\n".join([" & ".join(row) for row in row_array])

    return f"\\begin{{pmatrix}}\n{matrix_interior}\n\\end{{pmatrix}}"


print(NumpyToTex(np.random.rand(5,4), precision = 2))