import random 
from covariance import cov_matrix

def dot_product(v1, v2):
    return sum(x*y for x,y in zip(v1, v2))

def mat_vec_mult(matrix, vec):
    return [dot_product(row, vec) for row in matrix]

def normalize(vec):
    norm = sum(x ** 2 for x in vec)**0.5
    return [x / norm for x in vec]

'''
Using power iteration to approximate them
'''

def power_iteration(matrix, num_simulations = 1000):
    # Choose a random initial vector
    n= len(matrix)
    b_k= [random.random() for _ in range(n)]

    for _ in range(num_simulations):
        # Multiply by matrix
        b_k1 = mat_vec_mult(matrix, b_k)

        # Normalizes the vector
        b_k = normalize(b_k1)

    # Rayleigh quotient (estimate eigenvalue)
    eigenvalue = dot_product(mat_vec_mult(matrix, b_k), b_k) / dot_product(b_k, b_k)

    return eigenvalue, b_k

# Find the first eigenvalue and eigenvector
eigenvalue, eigenvector = power_iteration(cov_matrix)
print('Eigenvalue: ', eigenvalue)
print('eigenvector: ', eigenvector)