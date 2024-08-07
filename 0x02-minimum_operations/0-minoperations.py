#!/usr/bin/python3
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
    n_tmp = n
    for i in range(2, n):
        while (n_tmp % i == 0):
            op += i
            n_tmp /= i
        i+=1
    return op

