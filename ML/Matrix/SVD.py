import math

def transpose(A):
    # Returns the transpose of matrix A.
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def dot_product(x, y):
    # Returns the dot product of two vectors.
    return sum(x[i] * y[i] for i in range(len(x)))

def matrix_multiply(A, B):
    # Multiplies two matrices A and B.
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))
    return result

def identity_matrix(size):
    # Creates an identity matrix of a given size.
    I = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        I[i][i] = 1
    return I

def normalize_vector(V):
    # Normalizes vector V to unit length.
    norm = math.sqrt(sum(V[i] ** 2 for i in range(len(V))))
    return [V[i] / norm for i in range(len(V))]

def svd(A, tol=1e-10, max_iter=100):
    # Computes the Singular Value Decomposition of the matrix A.
    m, n = len(A), len(A[0])
    
    # Compute A^T A and A A^T
    AtA = matrix_multiply(transpose(A), A)
    AAt = matrix_multiply(A, transpose(A))

    # Initialize U and V
    U = identity_matrix(m)
    V = identity_matrix(n)

    # Jacobi iterative method for eigenvalue decomposition (on AtA for V)
    for _ in range(max_iter):
        for i in range(n):
            for j in range(i + 1, n):
                if abs(AtA[i][j]) > tol:
                    tau = (AtA[j][j] - AtA[i][i]) / (2 * AtA[i][j])
                    t = 1 / (abs(tau) + math.sqrt(1 + tau ** 2))
                    if tau < 0:
                        t = -t

                    c = 1 / math.sqrt(1 + t ** 2)
                    s = t * c

                    # Rotation to diagonalize AtA
                    for k in range(n):
                        Aik, Ajk = AtA[i][k], AtA[j][k]
                        AtA[i][k] = c * Aik - s * Ajk
                        AtA[j][k] = s * Aik + c * Ajk
                    for k in range(n):
                        Aki, Akj = AtA[k][i], AtA[k][j]
                        AtA[k][i] = c * Aki - s * Akj
                        AtA[k][j] = s * Aki + c * Akj
                    for k in range(n):
                        Vik, Vjk = V[k][i], V[k][j]
                        V[k][i] = c * Vik - s * Vjk
                        V[k][j] = s * Vik + c * Vjk
        
        # Break if AtA is diagonal enough
        if all(abs(AtA[i][j]) < tol for i in range(n) for j in range(i + 1, n)):
            break

    # Compute the singular values from the diagonal of AtA
    sigma = [math.sqrt(max(AtA[i][i], 0)) for i in range(n)]

    # Sort singular values and corresponding vectors
    sorted_indices = sorted(range(n), key=lambda k: sigma[k], reverse=True)
    sigma = [sigma[k] for k in sorted_indices]
    V = [[V[i][k] for k in sorted_indices] for i in range(n)]

    # Compute U from A A^T for rectangular matrices
    for j in range(min(m, n)):
        if sigma[j] > tol:
            U_col = [sum(A[i][k] * V[k][j] for k in range(n)) for i in range(m)]
            U_col = normalize_vector(U_col)
            for i in range(m):
                U[i][j] = U_col[i]
        else:
            for i in range(m):
                U[i][j] = 0

    return U, sigma, transpose(V)

def format_matrix(matrix):
    # Formats the matrix to the [[...]\n[...]] format.
    return "[[" + "]\n [".join([" ".join(f'{val:.8f}' for val in row) for row in matrix]) + ']]'


def format_vector(vector): # For orthogonal matrix
    formatted_matrix = '[\n'
    for row in vector:
        formatted_matrix += '['+' '.join(f'{val:.8e}' if val != 0 else '0' for val in row) + ']\n'
    formatted_matrix += ']'
    return formatted_matrix

def vector_to_diagonal_matrix(vector): # For Singular Value matrix
    if not hasattr(vector, '__iter__'):
        raise TypeError('Ínput must be an iterable, such as a list or an empty array.')
    
    size = len(vector)
    matrix = [[vector[i] if i== j else 0 for j in range(size)] for i in range(size)]
    return matrix 