#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:44:17 2018

@author: duzhe
"""

def max_heapify(A, n, i):
    
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)
        
def build_max_heap(A):
    n = len(A)
    for i in range((n//2), -1, -1):
        max_heapify(A, n, i)
        
def heap_sort(A):
    build_max_heap(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, i, 0)
        
A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
#arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
#max_heapify(A, 5, 1)
#max_heapify(arr, len(arr), 1)
#print(arr)
#build_max_heap(A)
heap_sort(A)
#print(A)
print(A)