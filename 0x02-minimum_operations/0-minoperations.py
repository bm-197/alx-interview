'''
A module for Alx interview min operation question.
'''
from math import sqrt


def minOperations(n):
    '''
     calculates the fewest number of operations
     needed to result in exactly n H characters in
     the file.
     '''
    op = 0
    for i in range(2, int((sqrt(n))) + 1):
        while (n % i == 0):
            op += i
            n /= i
    return op
