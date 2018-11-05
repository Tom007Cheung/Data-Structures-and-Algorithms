#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 08:49:26 2018

@author: duzhe
"""

def insertion_sort(A):
    for j in range(len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
        
A = [5, 2, 4, 6, 1, 3]
insertion_sort(A)
print(A)