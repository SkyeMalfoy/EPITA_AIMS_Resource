#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 2022/5/25  下午2:34
@Author: Skye
@File  : exam.py 
"""

# def sum(N):
#     result = 4
#     for i in range(N):
#         if N % 2 != 0:
#             add = -(4/(2*N-1))
#         else:
#             add = (4/(2*N-1))
#
#         result += add
#     print(result)
#
# sum(10000)
#
# def morseEncode(S):
#     morse ={'H': '0000', "E":'0', "L":'0100', "O":'111'}
#     result = str()
#     key_list = morse.keys()
#     for i in S:
#         if i in key_list:
#             result += (morse[i] + " ")
#         else:
#             return False
#     return result
# print(morseEncode("HE!LO"))
#
# def morseDecode(T):
#     morse = {'H': '0000', "E": '0', "L": '0100', "O": '111'}
#     result = str()
#     numbers_letter = str()
#     keys_list = []
#     values_list = []
#     for keys, values in morse.items():
#         keys_list.append(keys)
#         values_list.append(values)
#     for i in T+" ":
#         if i != " ":
#             numbers_letter += i
#             continue
#         if numbers_letter in values_list:
#             values_list_index = values_list.index(numbers_letter)
#             result += keys_list[values_list_index]
#             numbers_letter = ""
#         else:
#             return False
#     return result
# print(morseDecode("0000 0 0100 0100 111"))




import sys
sys.setrecursionlimit(100000)

def length(L):
    if length == None:
        return 0
    return length(L[1])+1

def contains(L, x):
    if L == None:
        return False
    return (L[0] == x or contains(L[1], x))

#First:
def chainedToOrdinary(L):
    if L == None:
        return []
    return [L[0]] + chainedToOrdinary(L[1])

#Second:
def chainedToOrdinary2(L):
    if L == None:
        return []
    else:
        R = [L[0]]
        T = chainedToOrdinary2(L[1])
        for x in T:
            R.append(x)
        return R

def invert(L, accumulator = None):
    if L is None:
        return accumulator
    else:
        return invert(L[-1], ((L[0]), accumulator))