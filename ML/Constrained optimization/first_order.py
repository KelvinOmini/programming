import numpy as np
from pernalized_funtion import multi_f


def f_dash(x_0, s_0, xm, multi_f, delta =1e-7):

    '''
    Compute rthe gradient directional derivative of a multivariable
    funtion 'multi_f' along with the search direction 'S_0' using the 
    central difference method.

    Args: 
        x_0 (numpy array): Starting point (vector).
        s_0 (numpy array): Search direction (vector).
        xm (float): Scalar multiplier for the search direction.
        multi_f (function): The multivariable funtion for which the 
        derivative is computed.
        delta (float): Step size for central difference (default is 1e-7).

    Returns: 
        f_(float): The directional derivatives (first-order differential) at
        'x_0' in the direction of 's_0'.
    '''

    # Dimension of the input vector 
    M = len(x_0)

    # Forward step
    xd_forward = np.copy(x_0) + (xm + delta) * s_0
    fdif = multi_f(xd_forward)

    # Backward step
    xd_backward =np.copy(x_0) + (xm - delta) * s_0
    bdif = multi_f(xd_backward)

    # Central difference
    f_ = (fdif - bdif) / (2 * delta)

    return f_
