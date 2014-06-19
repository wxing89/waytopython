#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Fibonacci series:
# the sum of two elements defines the text
a, b = 0, 1
while b < 1000:
    print b,
    a, b = b, a+b
