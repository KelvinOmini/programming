import numpy as np  # Import the NumPy library and alias it as np.
import matrix_approxi

class Matrix:  # Define a class named Matrix for handling matrix operations.
    
    def __init__(self, matrix1, matrix2, operation):  # Constructor method to initialize a Matrix object with two matrices and an operation.
        self.matrix1 = matrix1  # Store the first matrix.
        self.matrix2 = matrix2  # Store the second matrix.
        self.operation = operation  # Store the specified operation.

    def compute(self):  # Method to compute the result based on the specified operation.
        if self.operation == "+":  # Check if the operation is addition.
            result = self.add()  # Call the add method.
        elif self.operation == "-":  # Check if the operation is subtraction.
            result = self.subtract()  # Call the subtract method.
        elif self.operation == "*":  # Check if the operation is multiplication.
            result = self.multiply()  # Call the multiply method.
        elif self.operation == "/":  # Check if the operation is division.
            result = self.divide()  # Call the divide method.
        else:
            raise ValueError("Unsupported operation. Valid operations are '+', '-', '*', '/'.")  # Raise an error for unsupported operations.

        return result  # Return the computed result.
    
    @staticmethod
    def is_square(matrix):
        return len(matrix) == len(matrix[0])
    
    @staticmethod
    def is_equal_dimensions(matrix1, matrix2):
        return len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0])
    
    def add(self):  # Method to perform matrix addition.
        if not Matrix.is_equal_dimensions(self.matrix1, self.matrix2):  # Check if matrices have compatible dimensions.
            raise ValueError("Matrices must have the same dimensions for addition.")  # Raise an error for incompatible dimensions.
        
        result = []  # Initialize an empty list to store the result matrix.
        
        for i in range(len(self.matrix1)):  # Iterate over the rows of the first matrix.
            row = []  # Initialize an empty list to store a row of the result matrix.
            for j in range(len(self.matrix1[0])):  # Iterate over the columns of the first matrix.
                row.append(self.matrix1[i][j] + self.matrix2[i][j])  # Add corresponding elements from both matrices.
            result.append(row)  # Append the row to the result matrix.
        
        return result  # Return the result matrix.

    def subtract(self):  # Method to perform matrix subtraction.
        if len(self.matrix1) != len(self.matrix2) or len(self.matrix1[0]) != len(self.matrix2[0]):  # Check if matrices have compatible dimensions.
            raise ValueError("Matrices must have the same dimensions for subtraction.")  # Raise an error for incompatible dimensions.
        
        result = []  # Initialize an empty list to store the result matrix.
        
        for i in range(len(self.matrix1)):  # Iterate over the rows of the first matrix.
            row = []  # Initialize an empty list to store a row of the result matrix.
            for j in range(len(self.matrix1[0])):  # Iterate over the columns of the first matrix.
                row.append(self.matrix1[i][j] - self.matrix2[i][j])  # Subtract corresponding elements from both matrices.
            result.append(row)  # Append the row to the result matrix.
        
        return result  # Return the result matrix.

    def multiply(self):  # Method to perform matrix multiplication.
        if len(self.matrix1[0]) != len(self.matrix2):  # Check if matrices have compatible dimensions.
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication.")  # Raise an error for incompatible dimensions.
        
        result = []  # Initialize an empty list to store the result matrix.
        
        for i in range(len(self.matrix1)):  # Iterate over the rows of the first matrix.
            row = []  # Initialize an empty list to store a row of the result matrix.
            for j in range(len(self.matrix2[0])):  # Iterate over the columns of the second matrix.
                product = sum(self.matrix1[i][k] * self.matrix2[k][j] for k in range(len(self.matrix2)))  # Calculate the dot product of corresponding rows and columns.
                row.append(product)  # Append the product to the row of the result matrix.
            result.append(row)  # Append the row to the result matrix.
        
        return result  # Return the result matrix.

    def divide(self):  # Method to perform matrix division by a scalar.
        if len(self.matrix1[0]) != len(self.matrix2):  # Check if matrices have compatible dimensions.
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for division.")  # Raise an error for incompatible dimensions.
        # Calculate the inverse of matrix2
        matrix2_inv = np.linalg.inv(self.matrix2)  # Use NumPy to calculate the inverse of matrix2.
        # Perform matrix division by multiplying matrix1 with matrix2_inv
        result = np.dot(self.matrix1, matrix2_inv)  # Use NumPy to perform matrix multiplication.
        return result  # Return the result matrix.        

    def __str__(self):  # Method to define a string representation for the Matrix object.
        matrix1_string = '\n'.join([' '.join(map(str, row)) for row in self.matrix1])  # Convert the first matrix to a formatted string.
        matrix2_string = '\n'.join([' '.join(map(str, row)) for row in self.matrix2])  # Convert the second matrix to a formatted string.
        result_matrix = self.compute()  # Compute the result matrix based on the specified operation.
        result_string = '\n'.join([' '.join(map(lambda x: str(round(x, 2)), row)) for row in result_matrix])  # Convert the result matrix to a formatted string with rounded elements.

        return f"[{matrix1_string}] \n{self.operation} \n[{matrix2_string}]\n = \n[{result_string}]"  # Combine all representations into a final formatted string.

# For determinant calculations:
def determinant(matrix):
    # Get the size of the matrix (assuming it's a square matrix)
    size = len(matrix)

    # Base case: if the matrix is 1x1, return its only element
    if size == 1:
        return matrix[0][0]

    # Base case: if the matrix is 2x2, return the determinant using the formula
    # if size == 2:
    #     return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Initialize the determinant to 0
    det = 0

    # Perform cofactor expansion along the first row
    for i in range(size):
        # Calculate the cofactor by excluding the current row and column
        cofactor = matrix[0][i] * determinant([row[:i] + row[i + 1:] for row in matrix[1:]])

        # Alternate signs for each term in the expansion
        det += ((-1) ** i) * cofactor

    return det

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

while True:
    operationChoice = input("What specific matrix operation or computation are you looking to perform?:\n1. Determinant \n2. intrested in adding, subtracting, multiplying or dividing? \n3. Singuler Value Decomposition? \n4. Rank? \n5. matrix approximation?")
    if operationChoice == "1":
        print("You have choosen to find the determinant of a matrix.")
        # Get the matrix from user input
        matrix1 = get_matrix()

        # Check if the matrix is a square matrix before calculating determinant
        if not Matrix.is_square(matrix1):
            print("Error: The matrix must be a square matrix to calculate the determinant.")
        else:
            # Calculate and print the determinant
            det_result = determinant(matrix1)
            print(f"Determinant of the matrix: {det_result}")           

    elif operationChoice == "2":
        # Create the first matrix:
        matrix1 = []  # Initialize an empty list to store the first matrix.

        while True:  # Start an infinite loop for user input.
            try:
                row_input = input("Enter values for a row (i.e row (space) column) or type 'done' to finish: ")  # Prompt the user to enter values for a row.
                if row_input.lower() == 'done':  # Check if the user entered 'done' to finish input.
                    break  # Exit the loop if 'done' is entered.

                row_values = [int(value) for value in row_input.split()]  # Convert the input values to integers.
                matrix1.append(row_values)  # Append the row to the first matrix.

                if len(row_values) != len(matrix1[0]):  # Check if the number of columns in each row is the same.
                    print("Error: Number of columns in each row must be the same.")  # Print an error message.
                    matrix1.pop()  # Remove the invalid row.

            except ValueError:  # Handle the case where the user enters invalid integers.
                print("Error:        Please enter valid integers.")  # Print an error message.

        rows = len(matrix1)  # Get the number of rows in the first matrix.
        columns = len(matrix1[0]) if matrix1 else 0  # Get the number of columns in the first matrix if it is not empty, otherwise set it to 0.

        print(f"Your {rows} by {columns} matrix:")  # Display the dimensions of the first matrix.
        for row in matrix1:  # Iterate over the rows of the first matrix.
            print(row)  # Print each row of the first matrix.

        # Create the second matrix:
        matrix2 = []  # Initialize an empty list to store the second matrix.

        while True:  # Start an infinite loop for user input.
            try:
                row_input = input("Enter values for a row (i.e row (space) column) or type 'done' to finish: ")  # Prompt the user to enter values for a row.
                if row_input.lower() == 'done':  # Check if the user entered 'done' to finish input.
                    break  # Exit the loop if 'done' is entered.

                row_values = [int(value) for value in row_input.split()]  # Convert the input values to integers.
                matrix2.append(row_values)  # Append the row to the second matrix.

                if len(row_values) != len(matrix2[0]):  # Check if the number of columns in each row is the same.
                    print("Error: Number of columns in each row must be the same.")  # Print an error message.
                    matrix2.pop()  # Remove the invalid row.

            except ValueError:  # Handle the case where the user enters invalid integers.
                print("Error: Please enter valid integers.")  # Print an error message.

        rows = len(matrix2)  # Get the number of rows in the second matrix.
        columns = len(matrix2[0]) if matrix2 else 0  # Get the number of columns in the second matrix if it is not empty, otherwise set it to 0.

        print(f"Your {rows} by {columns} matrix:")  # Display the dimensions of the second matrix.
        for row in matrix2:  # Iterate over the rows of the second matrix.
            print(row)  # Print each row of the second matrix.

        while True:  # Start an infinite loop for user input.
            operation = input('Enter an operation: ')  # Prompt the user to enter an operation.
            if operation in ("+", "-", "*", "/"):  # Check if the entered operation is valid.
                result = Matrix(matrix1, matrix2, operation)  # Create a Matrix object with the specified matrices and operation.
                print(result)  # Print the result using the __str__ method of the Matrix class.
            else:
                print("Invalid operation. Please enter '+', '-', '*', or '/'.")  # Print an error message for invalid operations.
            
            choice = input("Would you like to continue with the same matrices? (yes/no) ")  # Prompt the user to continue or end the calculation.
            if choice.lower() == 'yes':  # Check if the user wants to continue.
                continue  # Continue the loop.
            elif choice.lower() == 'no':  # Check if the user wants to end the calculation.
                print("End of calculation!")  # Print a message indicating the end of the calculation.
                break  # Exit the loop.
            else:
                print('Invalid response')  # Print an error message for invalid responses.
                break  # Exit the loop.
    
    elif operationChoice == '3':
        matrix = get_matrix()
        U, S, V = SVD.svd(matrix)
        print(SVD.format_matrix(U), "\n") 
        print(SVD.vector_to_diagonal_matrix(S), "\n") 
        print(SVD.format_matrix(V))

    elif operationChoice == '4':
        Rank = rank.rank_of_matix(matrix)
        print('Rank of matrix:', Rank)

    elif operationChoice == '5':
        pass

    else:
        print("Invalid operation choice, try again!")
    decision = input("Would you like to continue using this calculator? (y/n): ")
    decision.upper()
    if decision == 'y':
        continue
    elif decision == 'n':
        break
    else:
        print("Invalid input\nswitching to default...")
        break

