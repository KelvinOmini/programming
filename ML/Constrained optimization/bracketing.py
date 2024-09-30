# The function bracketing_ implements the Bounding Phase Method, which is used
# to find an interval that contains the minimum point (Alpha*)
# during a unidirectional search along a search direction (S0)
# Starting from (x0).

import numpy as np

def bracketing_(x_0, s_0, uni_search, delta = 1e-7, w_0 = 0.5):
    '''
    Implements the bounding phase method to bracket the interval
    containing the minimum (Alpha*).

    Args: 
        x_0 (numpy array): Starting point vector.
        s_0 (numpy array): Search direction vector.
        uni_search (funtion): Unidirectionsal search funtion, whhich takes w,x, and s and returns function value.
        delta (float): Initial step size for perturbation (default is 1e-7) 
        w_0 (float): Initial guess for alpha (default is 0.5).

    Returns:
        (float, float): A tuple containing the interval (a,b) where the minimum Alpha* lies.
    '''

    k = 0 # Initialize step count

    # Step 1: Initial function evaluation for f0, fp, and fn
    f0 =uni_search(w_0, x_0, s_0, 0.0, 1.0)
    fp = uni_search(w_0 +delta, x_0, s_0, 0.0, 1.0)
    fn = uni_search(w_0 - delta, x_0,s_0, 0.0, 1.0)

    # Determine the direction of the next step based on initial comparisons
    if fn >= f0 >= fp:
        delta = abs(delta) # Move in the positive dirction
    elif fn <= f0 <= fp:
        delta = -abs(delta) # move in the negative direction
    else: 
        delta /= 2.0 # Reduce delta if no clear direction is found

    
    wn = w_0 - delta # Lower bound for the interval

    # Step 4: iteratively perturb to find upper bound w_1
    w_1 = w_0 + delta * 2**k
    f1 = uni_search(w_1, x_0, s_0, 0.0, 1.0)

    # Step 4: Iteratively expand the interval while f1 < f0
    while f1 < f0:
        k += 1
        wn = w_0
        w_0 = w_1
        f0 = f1
        w_1 = w_0 + delta * 2**k
        f1 = uni_search(w_1, x_0, s_0, 0.0, 1.0)

    a = wn # Lower bound 
    b = w_1 # Upper bound

    # Ensure (a, b) is correctly ordered based on the direction of the data
    if b < a:
        a, b = b, a # Swap if bounds are reversed

    return a, b
