def transpose(matrix: list):
    n = len(matrix)  # Number of rows/columns (assumes a square matrix)
    for i in range(n):
        for j in range(i+1, n):  # Only iterate over the upper triangle
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # Swap elements
