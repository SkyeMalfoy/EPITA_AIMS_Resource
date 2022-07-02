#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 2022/4/15  下午2:34
@Author: Skye
@File  : Exercise1.py
"""

import random
import time
def randomList(n):
    lst = []
    for i in range(n):
        num = random.randint(1, 100)
        lst.append(num)
    print(lst)
    return lst


#Seq: small to big
def bubbleSort(L):
    for i in range(len(L)-1):
        for j in range(len(L) - i - 1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    print(lst)

def merge(L):
    if len(L) == 1:
        return L
    else:
        mid = len(L) // 2
        left = L[:mid]
        right = L[mid:]
        return mergeSort(merge(left), merge(right))

def mergeSort(left, right):
    merged_lst = []
    while (len(left) > 0) and (len(right) > 0):
        if left[0] < right[0]:
            merged_lst.append(left.pop(0))
        else:
            merged_lst.append(right.pop(0))

    merged_lst += left
    merged_lst += right
    print(merged_lst)
    print(time.time())
    return merged_lst

lst = randomList(10)
# bubbleSort(lst)
merge(lst)

