from Least_Squares import matrix_multiply
from MLE import transpose, inverse

# Helper function to add two matrices
def matrix_add(A, B):
    result = [[0] * len(A[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]
    return result

# Helper function to create identity matrix 
def Identity_matrix(size):
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

# Helper function for scalar multiplication of a matrix
def Scalar_multiply(matrix, scalar):
    return [[scalar * elem for elem in row] for row in matrix]

# Function to raise a column of a matrix to a power
def column_power(matrix, col, power):
    return [row[col] ** power for row in matrix]

# Function to generate polynomial features manually 
def polynomial_features(X, degree):
    N = len(X)  # Number of samples
    D = len(X[0])  # Number of features per sample
    features = [[1] for _ in range(N)]  # Initialize N rows, each with a bias term (1)

    for d in range(1, degree + 1):
        for col in range(D):
            col_features = column_power(X, col, d)
            for i in range(N):
                features[i].append(col_features[i])

    return features

# Function to compute the MAP estimate for theta with linear features
def map_estimate_theta(X, y, sigma_squared, tau_squared):
    X_T = transpose(X)
    X_T_X = matrix_multiply(X_T, X)
    lambda_reg = sigma_squared / tau_squared
    I = Identity_matrix(len(X_T_X))

    lambda_I = [[lambda_reg * I[i][j] for j in range(len(I[0]))] for i in range(len(I))]
    addition = matrix_add(X_T_X, lambda_I)

    Inverse = inverse(addition)
    X_T_y = matrix_multiply(X_T, y)

    theta_MAP = matrix_multiply(Inverse, X_T_y)
    return theta_MAP

# Function to compute the MAP estimate for theta with non-linear features
def MAP_estimate_theta(X, y, degree, sigma_squared, tau_squared):
    Phi = polynomial_features(X, degree)
    Phi_T = transpose(Phi)
    Phi_T_Phi = matrix_multiply(Phi_T, Phi)
    lambda_reg = sigma_squared / tau_squared
    I = Identity_matrix(len(Phi_T_Phi))

    Phi_T_Phi_plus_lambda_I = matrix_add(Phi_T_Phi, Scalar_multiply(I, lambda_reg))

    try:
        Phi_T_Phi_plus_lambda_I_inv = inverse(Phi_T_Phi_plus_lambda_I)
    except NotImplementedError:
        raise NotImplementedError("Matrix inversion failed for sizes other than 2x2.")

    y = [[val] for val in y]  # Convert y to a column vector
    Phi_T_y = matrix_multiply(Phi_T, y)
    theta_map = matrix_multiply(Phi_T_Phi_plus_lambda_I_inv, Phi_T_y)

    return theta_map

# Sample data
X = [[1, 2], [3, 4], [5, 6]]  # N x D matrix (3 samples, 2 features)

# Parameters
Degree = 2
sigma_squared = 1  # Variance of the noise
tau_squared = 1    # Variance of the prior on theta

# User choice for linear or non-linear regression
choice = input('Linear or Non-linear: ')
if choice.lower() == 'linear':
    y = [[7], [9], [11]]  # N x 1 target vector (3 samples)
    theta_map = map_estimate_theta(X, y, sigma_squared, tau_squared)
    print(f"MAP estimate for theta: {theta_map}")

elif choice.lower() == 'non-linear':
    y = [7, 9, 11]  # N x 1 target vector (3 samples)
    theta_map = MAP_estimate_theta(X, y, Degree, sigma_squared, tau_squared)
    print(f"MAP estimate for theta with polynomial features: {theta_map}")
