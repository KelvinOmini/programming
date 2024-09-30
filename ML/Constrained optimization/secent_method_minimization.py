import numpy as np 
from first_order import f_dash

# Function to compute the 'z' in secent method formula
def compute_z(x_0, s_0, x1, x2, f_dash):
    '''
    Compute the next approximation 'z' using the secant method formula.

    Args: 
        x_0 (numpy array): Starting point vector.
        s_0 (numpy array): Search direction vector.
        x1 (float): lower bound 
        x2 (float): upper bound 
        f_dash (function): Funtion to compute the first-order derivative.

    Returns:
        z_(float): New approximation for the minima.
    '''

    z_ = x2 - ((x2 - x1) * f_dash(x_0, s_0, x2)) / (f_dash(x_0, s_0. x2) - f_dash(x_0, s_0, x1))
    return z_

# Secant Method to find the minimum
def secant_minima(a, b, x_0, s_0, f_dash, eps = 1e-7):
    '''
    Uses the secant method to find the optimal alpha (step size)
    that minimizes the function.

    Args: 
        a (float): Lower bound from the bounding phase method.
        b (float): Upper bound from the bounding phase method
        x_0 (numpy array): Starting point vector.
        s_0 (numpy array): Search direction vector
        f_dash (function): Function to compute the firs-order derivative.
        eps (float): Convergence tolerance for the derivative (default is 1e-7).

    Returns: 
        z (float): The optimal step size (alpha) minimizing the function.
    '''

    # Step 1: Initialize bounds
    x1 = a
    x2 = b

    # Stap 2: Compute new approximation for z
    z = compute_z(x_0, s_0, x1, x2, f_dash)

    # Step 3: Iteratively update z untill the derivative is close to zero (i.e convergence)
    while abs(f_dash(x_0, s_0, z)) > eps:
        if f_dash(x_0, s_0, z) >=0 :
            x2 = z # Eliminate the upperbound
        else: 
            x1 = z # Eliminate the lower bound

        # Recompute z using the updated bounds
        z = compute_z(x_0, s_0, x1, x2, f_dash)

    return z
 