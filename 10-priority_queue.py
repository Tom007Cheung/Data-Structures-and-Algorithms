#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:05:59 2018

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
        
def heap_maximum(A):
    return A[0]

def heap_extract_max(A, heap_size):
    if heap_size < 1:
        raise Exception("heap underflow")
        
    
    max = A[0]    
    A[0] = A[heap_size]
    heap_size = heap_size - 1
    max_heapify(A, heap_size, 1)
    
    return max

def heap_increase_key(A, i, key):
    if key < A[i]:
        raise Exception("new key is smaller than current key")
    A[i] = key
    parent = i // 2
    while i > 1 and A[parent] < A[i]:
        A[i], A[parent] = A[parent], A[i]
        i = parent
        
def max_heap_insert(A, heap_size, key):
    heap_size = heap_size + 1
    A[heap_size] = 0
    heap_increase_key(heap_size, key)