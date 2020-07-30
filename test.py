#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:54:14 2018

@author: michaelrickers
"""

# finding primes

import math

def finding_primes(p, q):
    prime_number_p = False
    prime_number_q = False
    while prime_number_p == False:
        for i in range(2, p):
            if (p % i) == 0:
                print(p, "is not a prime number: ")
                p = input("input a new p")
                p = int(p)
            else:
                print(p, "is a prime")
                prime_number_p = True        
    while prime_number_q == False: # seperate these
        for i in range(2, q):
            if (q % i) == 0:
                print(q, "is not a prime number: ")
                q = input("input a new q")
                q = int(q)
            else:
                print(q, "is a prime number)
                prime_number_q = True
    return p, q

test = finding_primes(4, 8)
print(test)

# better 


def finding_primes(p, q):
    p = input("input a new p")
    p = int(p)
    q = input("input a new q")
    q = int(q)
    prime_number_p = False
    prime_number_q = False
    while prime_number_p == False:
        for i in range(2, p):
            if (p % i) == 0:
                print(p, "is not a prime number: ")
                finding_primes(p, q)
            else:
                print(p, "is a prime")
                prime_number_p = True
                break
    while prime_number_q == False: # seperate these
        for i in range(2, q):
            if (q % i) == 0:
                print(q, "is not a prime number: ")
                finding_primes(p, q)
            else:
                print(q, "is a prime number")
                prime_number_q = True
                break
    return p, q

test = finding_primes(4, 8)
print(test)

# added rounding

import math

def finding_primes(p, q):
    p = input("input a new p")
    p = int(p)
    q = input("input a new q")
    q = int(q)
    prime_number_p = False
    prime_number_q = False
    while prime_number_p == False:
        for i in range(2, round(math.sqrt(p))):
            if (p % i) == 0:
                print(p, "is not a prime number: ")
                finding_primes(p, q)
            else:
                print(p, "is a prime")
                prime_number_p = True
                break
    while prime_number_q == False: # seperate these
        for i in range(2, round(math.sqrt(q))):
            if (q % i) == 0:
                print(q, "is not a prime number: ")
                finding_primes(p, q)
            else:
                print(q, "is a prime number")
                prime_number_q = True
                break
    return p, q

test = finding_primes(4, 8)
print(test)


# seperated p and q and p has to be smaller than q

import math

def finding_primes(p, q):
    p = input("input a new p")
    p = int(p)
    prime_number_p = False
    while prime_number_p == False:
        for i in range(2, round(math.sqrt(p))):
            if (p % i) == 0:
                print(p, "is not a prime number: ")
                finding_primes(p, q)
            else:
                print(p, "is a prime")
                prime_number_p = True
                break
    q = input("input a new q")
    q = int(q)
    prime_number_q = False
    if q > p:
        print("Please make q smaller than p") # this part not working post on piazza
        finding_primes(p, q)
    while prime_number_q == False: # seperate these
        for i in range(2, round(math.sqrt(q))):
            if (q % i) == 0:
                print(q, "is not a prime number: ")
                finding_primes(p, q)
            else:
                print(q, "is a prime number")
                prime_number_q = True
                break
    return p, q

test = finding_primes(4, 8)
print(test)
 
