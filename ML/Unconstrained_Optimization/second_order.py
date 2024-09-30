import numpy as np
import autograd.numpy as au
from autograd import grad, jacobian

def Himm(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 -7)**2

x_star = np.array([3, 2], dtype = 'float') # Local minimizer

# print('function at x_star: ', Himm(x_star))

# Now, we calculate the gradient vector and the Hessian 
# matrix of the function at x_star and look at the results.

# Gradient vector of the Himmelblau's function
Himm_grad = grad(Himm)
# print(f'Gradient vector at {x_star}: ', Himm_grad(x_star))

Himm_hess = jacobian(Himm_grad)
M = Himm_hess(x_star)
eigs = np.linalg.eigvals(M)
# print('The eigenvalues of M: ',eigs)

if (np.all(eigs>0)):
    print("M is positive definite")
elif (np.all(eigs >=0)):
    print('M is positive semi-definite')
else:
    print('M is negative definite')

