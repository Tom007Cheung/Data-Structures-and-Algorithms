#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 16:18:02 2018

@author: duzhe
"""
import random

def randomized_partition(A, p, r):
    i = random.randrange(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
        
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def randomized_quick_sort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quick_sort(A, p, q-1)
        randomized_quick_sort(A, q+1, r)
        
A = [5, 2, 4, 6, 1, 3]
randomized_quick_sort(A, 0, len(A)-1)
print(A)