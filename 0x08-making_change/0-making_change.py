#!/usr/bin/python3
""" A module for Solving MakeChange"""


def makeChange(coins, total):
    """  determine the fewest number of coins
    needed to meet a given amount total
    """
    if total <= 0:
        return 0
    
    rem = total
    c_cnt = 0
    c_idx = 0
    sorted_c = sorted(coins, reverse=True)
    n = len(sorted_c)

    while rem > 0:
        if c_idx >= n:
            return - 1
        
        if rem - sorted_c[c_idx] >=0:
            rem -= sorted_c[c_idx]
            c_cnt += 1
        else:
            c_idx += 1
    
    return c_cnt
