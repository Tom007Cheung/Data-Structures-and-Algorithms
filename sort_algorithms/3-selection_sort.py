#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 09:42:52 2018

@author: duzhe
"""

def selection_sort(A):
    n = len(A)
    for j in range(n-2):
        smallest = j
        for i in range(j + 1, n):
            if A[i] < A[smallest]:
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]

A = [5, 2, 4, 6, 1, 3]
selection_sort(A)
print(A)