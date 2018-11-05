#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:21:15 2018

@author: duzhe
"""

#def iterative_binary_search(A, v, low, high):
#    while low <= high:
#        mid = (low + high) // 2
#        if v == A[mid]:
#            return mid
#        elif v < A[mid]:
#            low = mid + 1
#        else:
#            high = mid - 1
#    return  None

def recursive_binary_search(A, v, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    if v == A[mid]:
        return mid
    elif v < A[mid]:
        return recursive_binary_search(A, v, mid+1, high)
    else:
        return recursive_binary_search(A, v, low, mid-1)
    
A = [5, 2, 4, 6, 1, 3]
n = len(A)
#print("iterative_binary_search: ",iterative_binary_search(A, 3, 0, n))
print("recursive_binary_search: ",recursive_binary_search(A, 3, 0, n))