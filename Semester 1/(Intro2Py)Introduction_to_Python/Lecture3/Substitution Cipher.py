#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 2022/4/25  下午3:53
@Author: Skye
@File  : Substitution Cipher.py 
"""
import random

# def CaesarCipher(N):
#     strings = "abcdefghijklmnopqrstuvwxyz "
#     dict_letters = {}
#     for i in strings:
#         if ord(i) + N == 123:
#             dict_letters[i] = " "
#         elif ord(i) + N > 123:
#             dict_letters[i] = chr(ord("a") + ord(i) - N - 123)
#         elif i == " ":
#             dict_letters[i] = chr(ord("a") + N - 1)
#         else:
#             dict_letters[i] = chr(ord(i) + N)
#     return dict_letters
#
# print(CaesarCipher(3))

# def CaesarCipher(N):
#     dict_letters = dict()
#     strings = "abcdefghijklmnopqrstuvwxyz "
#     for i in range(len(strings)):
#         dict_[strings[i]] = strings[(i + N) % len(strings)]
#     return dict_lettersletters

def randomCipher():
    strings = "abcdefghijklmnopqrstuvwxyz "
    dict_letters = {}
    for i in range(len(strings)):
        N = random.randint(0, len(strings) - 1)
        strings = strings[0: N] + strings[N+1 :]
        dict_letters[strings[i]] = strings[(i + N) % len(strings)]
    return dict_letters
print(randomCipher())

# def invertCipher(d):
#     d_new = {}
#     for keys in d.keys():
#         for values in d.values():
#             keys, values = values, keys
#             d_new[keys] = values
#     return d_new
# print(invertCipher(CaesarCipher(1)))

def invertCipher(d):
    iD = dict()
    for (k, v) in d.items():
        iD[v] = k
    return iD

#encrypt/decrypt
def encrypt(S, d):
    result = ""
    for c in S:
        result += d[c]
    return result

def decrypt(S, d):
    return decrypt(S, invertCipher(d))