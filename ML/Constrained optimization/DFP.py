import numpy as np
from bracketing import bracketing_
from secent_method_minimization import secant_minima
from central_difference import grad_multi_f

# DEP (Davidon-Flecher-Powell) method for unconstrained optimization
def DFP(x_ip, grad_multi_f, bracketing_, secant_minima, M=2, R=0.1, c = 1.55):
    '''
    Implement the DFP method to solve unconstrained optimization problem.

    Args:
        x_ip (numpy array): Initial guess for the solution.
        grad_multi_f (funtion): Function to compute the gradient.
        bracketing_ (function): Function for bounding phase method to find alpha bounds.
        secant_minima (function): Function to perform the secant minimization to find alpha*
        M (int): Dimensionally of the input vector (default is 2).
        R (float): Penalty parameter
        c (float): Factor to update penalty parameter R.

    Returns:
        x_1 (numpy array): The solution vector after optimization.
    '''

    # Tolerance for termination conditions
    eps1 = 1e-4
    eps2 = 1e-4
    max_iter = 50

    # Initialize variables
    grad0 = np.zeros(M)
    grad1 = np.zeros(M)
    xdiff = np.zeros(M)
    Ae = np.zeros(M)
    graddif = np.zeros(M)
    x_1 = np.zeros(M)
    x_2 = np.zeros(M)

    # Step 1: Initialize the iteration 
    k = 0
    x_0 = x_ip # Initial guess

    # Step 2: Compute initial search direction
    s_0 = np.zeros(M)  # Search direction
    grad0 = grad_multi_f(grad0, x_ip)
    s_0 = -grad0  # Initial search direction is the negative gradient
    
    # Step 3: Perform unidirectional search to find alphastar
    a, b = bracketing_(x_0, s_0)
    alphastar = secant_minima(a, b, x_0, s_0)
    
    for i in range(M):
        x_1[i] = x_0[i] + alphastar * s_0[i]
    
    grad1 = grad_multi_f(grad1, x_1)  # Compute the gradient at the new point

    # Step 4: Initialize the identity matrix for the Hessian approximation
    A = np.eye(M)  # Identity matrix
    dA = np.zeros((M, M))
    A1 = np.zeros((M, M))

    # Iteration loop
    for j in range(max_iter):  # Maximum iterations (50 here)
        k += 1
        
        # Compute the difference in position and gradient
        xdiff = x_1 - x_0 # Vector of position differences
        graddiff = grad1 - grad0

        # Update the Hessian approximation using the DFP formula
        dr = np.inner(xdiff, graddiff)
        for i in range(M):
            Ae[i] = 0
            for j in range(M):
                dA[i][j] = (xdiff[i] * xdiff[j]) / dr
                Ae[i] += A[i][j] * graddiff[j]

        dr = np.inner(graddiff, Ae)
        for i in range(M):
            for j in range(M):
                A1[i][j] = A[i][j] + dA[i][j] - (Ae[i] * Ae[j]) / dr
                A[i][j] = A1[i][j]

        # Step 5: Compute new search direction (s_1 = -A1 * grad1)
        s_1 = -A1 @ grad1 #Using matrix multiplication

        # Normalize the search direction
        unitv = np.linalg.norm(s_1)
        s_1 / unitv if unitv != 0 else 1 # Avoid division by zero

        # Perform unidirectional search to find alphastar along s_1
        a, b = bracketing_(x_1, s_1)
        alphastar = secant_minima(a, b, x_1, s_1)
        alphastar = round(alphastar, 3)  # Round alphastar to 3 decimal places
        
        # Update x_0 and x_1 for the next iteration
        x_0[:] = x_1 # Copy current x_1 to x_0
        x_1 += alphastar * s_1 # Update x_1 with new position

        # Step 6: Check for termination condition
        grad1 = grad_multi_f(grad1, x_1)
        grad0 = grad_multi_f(grad0, x_0)
        
        # Update the penalty parameter R if constaints are violated
        if any([g > 0 for g in x_1]):
            R *= c #Increase R by factor of c

        x_2 = x_1 - x_0 

        # Check if termination conditions are met
        if (np.linalg.norm(grad1) <= eps1) or (np.linalg.norm(x_2) / np.linalg.norm(x_0)) <= eps2:
            break

    return x_1


if __name__ == '__main__':
    # Example initial guess
    list = []
    list.extend([float(x) for x in input('Enter initial guess: ').split(',')])

    Dim = len(list)

    x_input_vector = np.array(list)

    # Define placeholder function for testing 
    def grad_multi_f(grad, x_input_vector):
        return np.array([2 * x_input_vector[i] for i in range(Dim)])
    
    def bracketing_(x_0, s_0):
        return 0.0, 1.0 
    
    def secant_minima(a, b, x_0, s_0):
        return 0.5
    
    # Run DEP
    solution = DFP(x_input_vector, grad_multi_f, bracketing_, secant_minima, Dim)
    print(f'Solution vector: {solution}')