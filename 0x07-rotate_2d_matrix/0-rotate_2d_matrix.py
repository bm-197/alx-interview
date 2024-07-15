#!/usr/bin/python3
""" A module for Rotating Matrix
"""
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """ A function that Rotates A matrix 90 degree.
    """
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        j, k = i, len(matrix) - i - 1
        while j < k:
            matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
            j += 1
            k -= 1
