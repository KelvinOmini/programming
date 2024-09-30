# Frobenius Norm Approximation
import math

def get_matrix():
    matrix = []  # Initialize an empty list to store the matrix.

    while True:
        try:
            row_input = input("Enter values for a row (space-separated) or type 'done' to finish: ")

            if row_input.lower() == 'done':
                break

            row_values = [float(value) for value in row_input.split()]  # Convert the input values to floats.
            if matrix and len(row_values) != len(matrix[0]):
                print("Error: Number of columns in each row must be the same.")
                continue

            matrix.append(row_values)  # Append the row to the matrix.
        except ValueError:
            print("Error: Please enter valid numbers.")

    return matrix

# Function to parse a matrix from a string
def parse_matrix(input_string):
    rows = input_string.strip().split(']')
    matrix = []
    for row in rows:
        cleaned_row = row.replace('[', '').strip()
        if cleaned_row:
            matrix.append([float(num) for num in cleaned_row.split()])
    return matrix

# Matrix multiplication function
def matrix_multiply(A, B):
    # Check if multiplication is possible
    if len(A[0]) != len(B):
        raise ValueError(f"Matrix multiplication not possible: A has {len(A[0])} columns but B has {len(B)} rows.")
    
    # Perform multiplication
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

# Transpose a matrix
def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

# Function to normalize a vector
def normalize_vector(V):
    norm = math.sqrt(sum(V[i] ** 2 for i in range(len(V))))
    return [V[i] / norm for i in range(len(V))]

# Singular Value Decomposition (SVD) function
def svd(A, tol=1e-10, max_iter=100):
    m, n = len(A), len(A[0])

    AtA = matrix_multiply(transpose(A), A)  # A^T * A
    AAt = matrix_multiply(A, transpose(A))  # A * A^T

    U = identity_matrix(m)
    V = identity_matrix(n)

    # Jacobi method for eigenvalue decomposition (on AtA for V)
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
                        Vik, Vjk = V[k][i], V[k][j]
                        V[k][i] = c * Vik - s * Vjk
                        V[k][j] = s * Vik + c * Vjk
        
        # Break if AtA is sufficiently diagonal
        if all(abs(AtA[i][j]) < tol for i in range(n) for j in range(i + 1, n)):
            break

    sigma = [math.sqrt(max(AtA[i][i], 0)) for i in range(n)]
    sorted_indices = sorted(range(n), key=lambda k: sigma[k], reverse=True)
    sigma = [sigma[k] for k in sorted_indices]
    V = [[V[i][k] for k in sorted_indices] for i in range(n)]

    for j in range(min(m, n)):
        if sigma[j] > tol:
            U_col = [sum(A[i][k] * V[k][j] for k in range(n)) for i in range(m)]
            U_col = normalize_vector(U_col)
            for i in range(m):
                U[i][j] = U_col[i]

    return U, sigma, transpose(V)

# Identity matrix function
def identity_matrix(size):
    I = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        I[i][i] = 1
    return I

# Convert vector to diagonal matrix
def vector_to_diagonal_matrix(vector):
    size = len(vector)
    matrix = [[vector[i] if i == j else 0 for j in range(size)] for i in range(size)]
    return matrix

# Format matrix for printing
def format_matrix(matrix):
    return "[[" + "]\n [".join([" ".join(f'{val:.8f}' for val in row) for row in matrix]) + ']]'

# Approximate matrix to rank k
def approximate_matrix(U, Sigma, VT, r):
    m, n = len(U), len(VT[0])
    k = min(r, m, n)

    while True:
        k_input = int(input(f'Choose a rank (k) between 1 and {r}: '))
        if 1 <= k_input <= r:
            k = k_input
            break
        else:
            print(f'Invalid rank! Please choose a rank between 1 and {r}.')

    # Since Sigma is a 1D vector, adjust for diagonal matrix construction
    Sigma_k = [[Sigma[i] if i == j and i < k else 0 for j in range(len(Sigma))] for i in range(k)]
    U_k = [[U[i][j] for j in range(k)] for i in range(m)]
    VT_k = [[VT[i][j] for j in range(n)] for i in range(k)]

    USigma_k = matrix_multiply(U_k, Sigma_k)
    A_k = matrix_multiply(USigma_k, VT_k)

    return A_k

# Main part
matrix = get_matrix()
Rank = len(matrix[0])  # Simplified rank calculation
U, S, VT = svd(matrix)

print("U matrix:")
print(format_matrix(U))
print("\nSigma (Singular values) matrix:")
print(format_matrix(vector_to_diagonal_matrix(S)))
print("\nVT matrix:")
print(format_matrix(VT))

Approximate_rank = approximate_matrix(U, S, VT, Rank)
print("\nApproximated Matrix:")
for row in Approximate_rank:
    print(row)
