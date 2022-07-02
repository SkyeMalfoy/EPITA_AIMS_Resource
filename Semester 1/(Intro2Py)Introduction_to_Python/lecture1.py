#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 2022/4/6  下午2:55
@Author: Skye
@File  : lecture1.py 
"""

# #1. sum
# def sum(N):
#     sum = 0
#     for i in range(1, N+1):
#         sum += i
#     print(sum)
# sum(10)

#1.1 sum using recursive:

#
# #2.table
# def table(N):
#     for i in range(1,11):
#         print(i + "*" + N + " = " + (i*N))
# table(9)

#3.isPrime(N)
# def isPrime(N):
#     for i in range(2, N):
#         if N == 1 or N == 2:
#             return False
#         if N % i == 0:
#             return False
#         else:
#             if i < N-1:
#                 continue
#             else:
#                 return True
#
# N = 12
# flag = isPrime(N)
# print("number " + str(N) + ": " + str(flag))

# #4. pay(N):
# def pay(N):
#     while True:
#         if N >= 2.0:
#             N -= 2.0
#             print("2 euros.")
#         elif N >= 1.0:
#             N -= 1.0
#             print("1 euro.")
#         elif N >= 0.5:
#             N -= 0.5
#             print("50 cents.")
#         elif N >= 0.2:
#             N -= 0.2
#             print("20 cents.")
#         elif N >= 0.1:
#             N -= 0.1
#             print("10 cents.")
#         elif N >= 0.05:
#             N -= 0.05
#             print("5 cents.")
#         elif N >= 0.02:
#             N -= 0.02
#             print("2 cents.")
#         elif N == 0.01:
#             N -= 0.01
#             print("1 cent.")

# #
# N = float(input("please input a payment:"))
# pay(N)

# 5.primeNumberDecomposition(N)
# def primeNumberDecomposition(N):
#     i = 2
#     while i <= N:
#         if N == 1:
#             return print('1')
#         elif N == 2:
#             return print('1\n2')
#         else:
#             if N % i != 0:
#                 return print('1\n' + str(N))
#             elif N % i == 0:
#                 N /= i
#                 print(int(i))
#                 continue
#             else:
#                 i += 1
#                 continue
#             print(int(N))
#
# primeNumberDecomposition(100)

# 6. toBinary(N)
# def toBinary(N):
#     N_bin = ""
#     while True:
#         if N % 2 == 0:
#             N_bin += "1"
#             N /= 2
#             continue
#         elif N == 1:
#             N_bin += "1"
#             break
#         else:
#             N_bin += "0"
#             N = round(N/2)
#             continue
#
#     return N_bin
# print(toBinary(19))

#7.Prime number dec
def process(N, current_prime = 2, current_power = 0, result = ""):
    if current_prime > N/2:
        if result == "":
            return str(current_prime) + "^" + str(current_power + 1)
        else:
            return result + str(int(N)) + "^1"
    if N % current_prime == 0:
        return process(N/current_prime, current_prime, current_power + 1, result)
    if current_power == 0:
        return process(N, current_prime + 1, 0, result)
    else:
        return process(N, current_prime + 1, 0, result + str(current_prime) + "^" + str(current_power) + "*")

print(process(8))