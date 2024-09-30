def swap_rows(matrix, row1, row2, col):
    for i in range(col):
        matrix[row1][i], matrix[row2][i] = matrix[row2][i], matrix[row1][i]

def rank_of_matrix(matrix):
    rows =len(matrix)
    cols = len(matrix[0])
    rank = cols

    for r in range(rank):
        # If the leading element is zero, search for a non-zero element in the same column
        if matrix[r][r] == 0:
            for i in range(r + 1, rows):
                # Swap rows if a non-zero element is found
                if matrix[i][r] != 0:
                    swap_rows(matrix, r, i, cols)
                    break
            else:
                # If no non-zero element is found, reduce the rank by one and adjust the column.
                rank -= 1
                for i in range(rows):
                    matrix[i][r], matrix[i][rank] = matrix[i][rank], matrix[i][r]
                continue

        for i in range(r + 1, rows):
            multiplier = matrix[i][r] / matrix[r][r]
            for j in range(rank):
                matrix[i][j] -= multiplier * matrix[r][j]

    non_zero_rows = 0
    for row in matrix:
        if any([abs(x) > 1e-10 for x in row]):
            non_zero_rows +=1
    return non_zero_rows

