# This function uses the central difference method to calculate
# the gradient vector at a particular point in search space.
import numpy as np
from pernalized_funtion import multi_f

def grad_multi_f(multi_f, x_ip, delta_=0.001):
    '''
    Computes the gradient of the function 'multi_f' at the point 'x_ip'
    using the central finite difference method.

    Arg: 
        multi_f(function): The function for which to compute the gradient.
        x_ip(numpy array): Input point (vector) where the gradient is computed.
        delta_(float): Step size for finite difference (default is 0.001),

    Returns: 
        grad(numpy array): The gradietnt vector at the point 'x_ip'
    '''

    M = len(x_ip) # dimension of the input vector
    grad = np.zeros(M) # Initialize gradient 

    for i in range(M):
        # Creating d1 and d2 copies of x_ip
        d1 = np.copy(x_ip)
        d2 = np.copy(x_ip)

        # Modify the i-th component by adding and subtracting delta_
        d1[i] += delta_
        d2[i] -= delta_

        # Compute the central finite difference
        fdiff =  multi_f(d1)
        bdiff = multi_f(d2)
        grad[i] = (fdiff -bdiff) / (2 * delta_)

    return grad

