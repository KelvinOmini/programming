from Least_Squares import matrix_multiply

# Helper function to compute matrix transpose
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed

# Helper function to compute determinant of a matrix
def determinant(matrix):
    # Base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursive case for larger matrices
    det = 0
    for col in range(len(matrix)):
        # Create the cofactor matrix by removing first row and col-th column
        cofactor_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(cofactor_matrix)

    return det

# Helper function to compute cofactor matrix
def cofactor(matrix):
    cofactors = []
    for row in range(len(matrix)):
        cofactor_row = []
        for col in range(len(matrix)):
            minor = [r[:col] + r[col+1:] for r in (matrix[:row] + matrix[row+1:])]
            cofactor_row.append(((-1) ** (row + col)) * determinant(minor))
        cofactors.append(cofactor_row)
    return cofactors

# Helper function to compute inverse of a matrix
def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError('Matrix is singular and cannot be inverted')
    
    cofactors = cofactor(matrix)
    adjugate = transpose(cofactors)
    return [[adjugate[row][col] / det for col in range(len(matrix))] for row in range(len(matrix))]

# Function to compute optimal theta for least squares
def optimal_theta(X, y):
    '''
    Step 1: Compute X^T 
    Step 2: Compute X^T * X
    Step 3: Compute inverse of X^T * X
    Step 4: Compute X^T * y
    Step 5: Compute the optimal theta: (X^T * X)^(-1) * X^T * y
    '''
    X_T = transpose(X)
    X_T_X = matrix_multiply(X_T, X)
    X_T_X_inv = inverse(X_T_X)
    X_T_y = matrix_multiply(X_T, y)
    theta = matrix_multiply(X_T_X_inv, X_T_y)
    return theta

# Sample data
X = [[1, 2], [3, 4], [5, 6]]  # N x D matrix (3 samples, 2 features)
y = [[7], [9], [11]]           # N x 1 target vector (3 samples)

# Compute the optimal theta
theta_opt = optimal_theta(X, y)
print(f"Optimal Theta: {theta_opt}")
