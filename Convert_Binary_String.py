#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:54:34 2018

@author: michaelrickers
"""

def Convert_Binary_String(x): # takes an integer as only argument
    '''This function takes in an integer and returns a binary representation as a string'''
    l = [] # initializes an empty list
    k = 0 # sets temporary variable for k
    empty_str = '' # initializes empty string
    while x > 0: # creates while loop while integer is bigger than 0
        k = x % 2 # gets remainder after taking modulo 2
        l.insert(0, k) # inserts bit representation at index 0
        x = x // 2 # uses integer division to get next x value, and repeat loop
    for i in l: # loops through list l
        i = str(i) # changes integer values of i to string characters
        empty_str = empty_str + i # adds string values of bits to empty string
    return empty_str # returns binary representation of integer as a string
    
    
    

test = Convert_Binary_String(644)

print(test)
print(type(test))

#l_ist = [1, 1, 0, 0, 1]
#l_ist = ''.join(l_ist)
#
#print(l_ist)

#empty_str = ''
#for i in l_ist:
#    i = str(i)
#    empty_str = empty_str + i

#print("maybe", empty_str)
#l_ist = str(l_ist)
#l_ist = ''.join(l_ist)
#
#print("yes?", l_ist)
#print(type(l_ist))