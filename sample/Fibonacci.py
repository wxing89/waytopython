#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Fibonacci series:
# the sum of two elements defines the text

# write Fibonacci series up to n
def fib(n):
    '''Print a Fibonacci series up to n.'''
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

# Now call the function we just defined:
fib(2000)

