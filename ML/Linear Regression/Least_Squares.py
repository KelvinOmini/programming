# Matrix multiplication function
def matrix_multiply(A, B):
    # Check if multiplication is possible
    if len(A[0]) != len(B):
        raise ValueError(f"Matrix multiplication not possible: A has {len(A[0])} columns but B has {len(B)} rows.")
    
    # Perform multiplication
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

# Helper function to subtract two vectors/matrices
def vector_substract(A,B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Helper function to compute the squared norm of a vector
def squared_norm(vector):
    return sum([vector[i][0] ** 2 for i in range(len(vector))])

# Function to compute the least squares loss
def least_square_loss(X, y, theta, sigma2):
    '''
    Step 1: Compute X * Theta
    step 2: Compute y - x * theta
    step 3: Compute the squared norm of  (y - x * theta)
    step 4: Compute the loss
    '''

    X_theta = matrix_multiply(X, theta)
    diff = vector_substract(y, X_theta)
    norm_squared = squared_norm(diff)
    loss = (1 / (2 * sigma2)) * norm_squared
    return loss



N = 3  # number of data points
D = 2  # number of features

X = [[1, 2], [3, 4], [5, 6]]  # Example input matrix (N x D)
y = [[7], [9], [11]]           # Example target vector (N x 1)
Theta = [[0.5], [1.0]]         # Example parameter vector (D x 1)
sigma2 = 1.0                   # Example variance of the error term


# Compute the loss
loss = least_square_loss(X, y, Theta, sigma2)
print(f"Loss: {loss}")
