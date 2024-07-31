#!/usr/bin/python3
""" Module For Island Perimeter."""


def islandPerimeter(grid):
    """ Island Perimeter Solver."""
    size = 0
    edges = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                size += 1
                if j > 0 and grid[i][j - 1]:
                    edges += 1
                if i > 0 and grid[i - 1][j]:
                    edges += 1

    return size * 4 - edges * 2

