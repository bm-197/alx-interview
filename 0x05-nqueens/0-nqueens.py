#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing 
N non-attacking queens on an NxN chessboard. Write 
a program that solves the N queens problem.
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

def print_solution(solution):
    positions = []
    for i in range(N):
        for j in range(N):
            if solution[i][j] == 'Q':
                positions.append([i, j])
    print(positions)

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve(board, col):
    if col >= N:
        solns.append([row[:] for row in board])
        return

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 'Q'
            solve(board, col + 1)
            board[i][col] = '.'

    return


board = [['.' for _ in range(N)] for _ in range(N)]
solns = []
solve(board, 0)

for soln in solns:
    print_solution(soln)
