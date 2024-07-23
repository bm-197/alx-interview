#!/usr/bin/python3
"""
A module for working with Pascal's triangle.
"""
def pascal_triangle(n):
    """
    Function to calculate Pasacals Triangle.
    
    Args:
        n (int) : number of rows of the triangle
    Return:
        List(List(int)): The triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(0, n-1):
        row = triangle[i]
        tri = [1]
        for j in range(len(row) - 1):
            tri.append(row[j] + row[j + 1])
        tri.append(1)
        triangle.append(tri)

    return triangle
