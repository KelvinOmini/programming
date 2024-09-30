# _Matrix Approximation with SVD and User Selected rank k
def parse_matrix(input_string):
    if isinstance(input_string, list):
        raise ValueError('Input should be a string, not a list')
    
    rows = input_string.strip().split(']')
    matrix = []
    for now in rows:
        cleaned_row = rows.replace('[', '').replace(']','').strip()
        if cleaned_row:
            matrix.append([float(num) for num in cleaned_row.split()])
    return matrix

def get_dimensions(matrix):
    return len(matrix), len(matrix[0])

def matrix_multiply(A, B):
    result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    return result

def approximate_matrix(U, Sigma, VT, r):
    m, n = get_dimensions(U)

    rank = min(m,n)

    while True:
        k = int(input(f'Choose a rank (k) between 1 and {r}:'))
        if 1 <= k <= r:
            break
        else:
            print(f'Invalid rank! Please choose a rank between 1 and {r}.')

    # Create Sigma_k by keeping only the first k singular values
    Sigma_k = [[Sigma[i][i] if i==j  and i < k else 0 for j in range(len(Sigma))] for i in range(len(Sigma))]

    # Create U_k by keeping only the first k columns of U
    U_k = [[U[i][j] for j in range(k)] for i in range(len(U))]

    # Create V_k^T by keeping only the first k rows of V^T
    VT_k = [[VT[i][j] for j in range(len(VT[0]))] for i in range(k)]

    USigma_k = matrix_multiply(U_k, Sigma_k) # U_k * Sigma_k
    A_k = matrix_multiply(USigma_k, VT_k) # (U_k * sigma_k) * V_k^T

    return A_k