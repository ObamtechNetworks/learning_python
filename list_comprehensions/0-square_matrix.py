def square_matrix_simple(matrix=[]):
    if not matrix:
        return []
    if isinstance(matrix[0], int):
        # Handle 1D array
        if all(isinstance(x, int) for x in matrix):
            return [[x ** 2] for x in matrix]
        else:
            raise ValueError("Invalid element in 1D array")

    elif all(isinstance(row, list) for row in matrix):
        # Handle 2D array
        if all(isinstance(x, int) for row in matrix for x in row):
            return [[x ** 2 for x in row] for row in matrix]
        else:
            raise ValueError("Invalid element in 2D array")

    else:
        raise ValueError("Invalid input")
