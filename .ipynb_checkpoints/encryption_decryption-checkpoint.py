#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 11:22:12 2018

@author: michaelrickers
"""

def encryption(m, e, n):
    c = 0
    c = m ** e % n
    return c

def decryption(c, d, n):
    m = 0
    m = c ** d % n
    return m

test = encryption(1819, 13, 2537)
print(test)   

test_d = decryption(1317, 937, 2537)
print("d", test_d)
