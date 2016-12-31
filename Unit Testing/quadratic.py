import math  # For math over the reals
import cmath # For math over the complex numbers

def roots(a, b, c):
    ''' Our first attempt at creating a function that calculates the roots 
        of a quadratic '''
    # A quadratic function can have either one or two real/complex roots
    x_1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
    x_2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a

    # We'll return these values in a tuple
    if x_1 == x_2:
        return (x_1)
    else:
        return (x_1, x_2)
        
def roots_corrected(a, b, c):
    ''' The second version which works with complex numbers as well '''
    x_1 = (-b + cmath.sqrt(b**2 - 4*a*c))/2*a
    x_2 = (-b - cmath.sqrt(b**2 - 4*a*c))/2*a

    if x_1 == x_2:
        return (x_1)
    else:
        return (x_1, x_2)