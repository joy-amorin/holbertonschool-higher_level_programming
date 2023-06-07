#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_m = matrix.copy()
    square = list(map(lambda row: list(map(lambda x: x ** 2, row)), new_m))

    return square
