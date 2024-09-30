# This function takes an input vector x (a point in search
# space) and returns the function value (penalized function value)
# at thast point

import numpy as np

eps = 1e-6
delta = 1e-3
nc = 1 #number of constraints
g = np.zeros(nc)
r = 10 # Penalty Scaling factor 

'''def multi_f(x):
    # Himmelbiau Function (Objective Function)
    sum_ = (x[0]**2 + x[1] - 11)**2 + (x[1]**2 + x[0] -7)**2

    # Constraints (g(x) should be >=0 to satisfy constraints)
    g[0] = -26.0 + (x[0] - 5.0)**2 + x[1]**2

    for i in range(nc):
        if (g[i] < 0.0): # constraint is violated.
            sum_ += r*g[i]**2 # Add penality based on the violation
    return sum_
'''
# Modified multi_f that incorporate the penalty parameter R
def multi_f(x, R):
    '''
    Compute the penalized objective function value

    Args:
        x (numpy array): The current input vector
        R (float): Penalty parmeter.

    Returns: 
        float: Penalized objective function value.
    '''

    # Himmelblau's function (example objective)
    sum_ = (x[0]**2 + x[1] - x[1] - 11)**2 + (x[1]**2 + x[0] - 7)**2

    # Constraint: g(x) <= 0 (example constraint)
    g = -26.0 + (x[0] - 5.0)**2 + x[1]**2 

    if g >0 : # Violation occurs when g(x) > 0
        sum_ += R * g**2

    return sum_