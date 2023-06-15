#!/usr/bin/python3
""" divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """function to divides elements """
    size_r = len(matrix[0])
    for row in matrix:
        if len(row) != size_r:
            raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            if type(i) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if type(div) not in (int, float):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            # 'round' to rounded 2 decimal
            new_row.append(round(i / div, 2))
        new_matrix.append(new_row)
    return new_matrix
