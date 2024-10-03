def mean_center(x):
    mean_vector = [sum(col) / len(col) for col in zip(*x)] # Compute-wise mean
    centered_data = [[x[i][j] - mean_vector[j] for j in range(len(x))] for i in range(len(x))]
    return centered_data #, mean_vector

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

def main():
    X = get_matrix()
    x_centered = mean_center(X)
    print(f'Mean Centered Data: ', x_centered)

if __name__ == '__main__':
    main()
