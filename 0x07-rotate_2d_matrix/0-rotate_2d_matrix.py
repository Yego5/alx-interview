#!/usr/bin/python3
'''
module:
rotate 2D Matrix
'''


def rotate_2d_matrix(matrix):
    '''
    rotates a given 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of lists): The 2D matrix to be rotated.

    returns:
        None
    '''
    n = len(matrix)

    # transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
