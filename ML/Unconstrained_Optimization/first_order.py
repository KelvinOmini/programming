import numpy as np
import scipy

# Importing the Rosenbrock funtion, its gradient and Hessian respectively
from scipy.optimize import rosen, rosen_der, rosen_hess
x_m = np.array([1,1]) # Given local minimizer
print(rosen(x_m)) #Check x_m is minimizer 

print(rosen_der(x_m)) # Calculate the gradient at the point x_m
