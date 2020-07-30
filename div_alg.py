#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:35:10 2018

@author: michaelrickers
"""

def div_alg(a, d):
    '''Takes two integers and a and d and returns the quotient and remainder'''
    q = 0 # initialize the quotient as 0
    assert d > 0  # assert d has to be larger than 0
    if a > 0: # if a is positive plug it in for r
        r = a 
    else:  # if a is negative take absolute value of it
        r = a * -1
    while r >= d:  
        r = r - d
        q = q + 1
    if a < 0 and r > 0:
        r = d - r
        q = -1 * (q + 1)
    return q, r

test = div_alg(7, 4)

print(test)