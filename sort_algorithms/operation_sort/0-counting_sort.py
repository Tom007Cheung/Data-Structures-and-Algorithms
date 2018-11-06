#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 09:04:48 2018

@author: duzhe
"""

def counting_sort(A, B, k):
    C = [0] * (k+1)
#    for i in range(k):
#        C[i] = 0
    for j in range(len(A)):
        C[A[j]] += 1
    for i in range(1, k+1):
        C[i] += C[i-1]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
        

A = [2, 5, 3, 0, 2, 3, 0, 3]
#B = A   wrong
B = [0] * (8)
print(B)
k = 5
counting_sort(A, B, k)
print(A)
print(B)