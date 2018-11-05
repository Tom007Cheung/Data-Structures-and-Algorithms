#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:11:13 2018

@author: duzhe
"""

def bubble_sort(A):
    for i in range(len(A)-2):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                
A = [5, 2, 4, 6, 1, 3]
bubble_sort(A)
print(A)