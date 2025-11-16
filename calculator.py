"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    raise ZeroDivisionError if a == 0 
    return b / a    
    
def logarithm(a, b): 
    return loga(b)
    # use math library/raise ValueError

def exponent(a, b): 
    return ab
