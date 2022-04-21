import numpy as np
import fractions

def format_element_(x, precision = 2, force_frac = False, max_denom = 100, upright = False, **kwargs):
    '''
        Properly convert an input to a string for matrix output.

        param x np.ndarray : Input value
        param precision int (default = 2): Rounding precision
        param force_frac bool (default = True) : If True, all outputs will be fractions.
        param max_denom int (default = 100) : The maximium denominator for fractions.
        param upright bool (default = False) : If true, we write fractions with \frac{}{}    
    
    '''

    if (force_frac and max_denom is None):
        raise Exception("When force_frac = True, a value for denom_limit must be passed in.")

    x_frac = fractions.Fraction(x).limit_denominator(max_denominator=max_denom)

    if (force_frac or np.isclose(x, x_frac.numerator/x_frac.denominator)):
        if (x_frac.numerator == 0):
            return "0"
        if (upright):
            return f"\\frac{{{x_frac.numerator}}}{{{x_frac.denominator}}}"
        
        return f"{x_frac.numerator}/{x_frac.denominator}"
        

    if (np.isclose(x, 0, **kwargs)):
        return "0"
    else:
        return str(round(x, precision))

def NumpyToTex(M, precision = 2, force_frac = False, max_denom = 100, upright = False, **kwargs):
    '''
    Prints M nicely to be pasted directly into LaTeX.
    
    param M np.ndarray : Input matrix
    param precision int (default 2) : Rounding precision
    param atol, rtol float : Passed into np.isclose.
    
    '''
    assert len(M.shape) <= 2, "Cannot convert ndarray of dimensionality > 2 into LaTeX."

    if (len(M.shape) == 1):
        M = M.reshape(-1, 1)

    func = lambda x: format_element_(x, precision = precision, force_frac = force_frac, max_denom = max_denom, upright = upright, **kwargs)

    row_array = [[func(element) for element in row] for row in M]

    matrix_interior = " \\\\\n".join([" & ".join(row) for row in row_array])

    return f"\\begin{{pmatrix}}\n{matrix_interior}\n\\end{{pmatrix}}"

