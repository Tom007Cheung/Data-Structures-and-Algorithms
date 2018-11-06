#!/usr/bin/env lython3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:29:28 2018

@author: duzhe
"""
import sys
    
def merge(A, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1+1)
    R = [0] * (n2+1)
    for i in range(n1):
        L[i] = A[l+i]
    for j in range(n2):
        R[j] = A[m+1+j]
    L = sys.maxsize
    R = sys.maxsize
    i = 0
    j = 0
    for k in range(l, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def merge_sort(A, l, r):
    if l < r:
        m = l + (r-l) // 2
        merge_sort(A, l, m)
        merge_sort(A, m+1, r)
        merge(A, l, m, r)
            
A = [5, 2, 4, 6, 1, 3]

n = len(A)

merge_sort(A, 0, n)

print(A)