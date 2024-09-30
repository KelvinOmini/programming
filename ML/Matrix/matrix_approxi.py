# Frobenius Norm Approximation
import Matrix.approxi as approxi
import Matrix.rank as rank
import Matrix.SVD as SVD


def get_matrix():
    matrix = []  # Initialize an empty list to store the matrix.

    while True:
        try:
            row_input = input("Enter values for a row (space-separated) or type 'done' to finish: ")
            
            if row_input.lower() == 'done':
                break

            row_values = [int(value) for value in row_input.split()]  # Convert the input values to integers.
            matrix.append(row_values)  # Append the row to the matrix.

            if len(row_values) != len(matrix[0]):
                print("Error: Number of columns in each row must be the same.")
                matrix.pop()  # Remove the invalid row.

        except ValueError:
            print("Error: Please enter valid integers.")

    return matrix

matrix = get_matrix()
Rank = rank.rank_of_matrix(matrix)
U, S, V = SVD.svd(matrix)
print(SVD.format_matrix(U), "\n") 
print(SVD.vector_to_diagonal_matrix(S), "\n") 
print(SVD.format_matrix(V))

Parsed_U = approxi.parse_matrix(U)
Parsed_S = approxi.parse_matrix(S)
parsed_VT = approxi.parse_matrix(V)

Approximate_rank = approxi.approximate_matrix(Parsed_U, Parsed_S, parsed_VT, Rank)
for row in Approximate_rank:
    print(row)

