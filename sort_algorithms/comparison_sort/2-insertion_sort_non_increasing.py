#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 09:13:44 2018

@author: duzhe
"""

def insertion_sort_non_increasing(A, n):
    for j in range(n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] < key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

A = [5, 2, 4, 6, 1, 3]
n = len(A)
insertion_sort_non_increasing(A, n)
print(A)