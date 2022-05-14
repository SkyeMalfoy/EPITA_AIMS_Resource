#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 2022/4/15  下午4:54
@Author: Skye
@File  : binary tree.py 
"""
import random
def height(T):
    # If T is an empty tree
    if T == None:
        return 0
    #If not
    (lc, label, rc) = T
    return 1 + max(height(lc), height(rc))
#
# print(height(((None,"b",None), "a", (None,"b",None))))


# def nbElements(T):
#     if T == None:
#         return 0
#     else:
#         (lc, label, rc) = T
#         return 1 + nbElements(lc) + nbElements(rc)
#
# print(nbElements(((None,"b",None), "a", (None,"b",None))))


# def randomTree(branchingProbability = 0.75, maxHeight = 5, label = 0):
#     if random.random() > branchingProbability or maxHeight <= 1:
#         lc = None
#     else:
#         lc = randomTree(maxHeight=maxHeight - 1, label=random.randint(1, 100))
#
#     if random.random() > branchingProbability or maxHeight <= 1:
#         rc = None
#     else:
#         rc = randomTree(maxHeight=maxHeight - 1, label=random.randint(1, 100))
#     return lc, label, rc
#
# lc, label, rc = randomTree()
# print((lc, label, rc))


# def isMember(T, x):
#     if T == None:
#         return False
#     else:
#         (lc, label, rc) = T
#         return (label == x) or isMember(rc, x) or isMember(lc, x)
#
# judge = isMember(((None, "b", None),"a", None), "b")
# print(judge)

#popTree
# def popTree(T, height):
#      (lc, label, rc) = T
#      if height == 0:
#         return None
#      elif height == 1:
#         return T
#      else:
#          height -= 1
#          return popTree(rc, height)
#
# T = ((None, "b", None), "a", (None, "c", None))
# print(popTree(T, height(T)))

# def popTree(T):
#     if T == None:
#         return (None, None)
#     else:
#         (lc, label, rc) = T
#         if rc == None:
#             return (label, lc)
#         else:
#             (rightmost_of_rc, resulting_rc) = popTree(rc)
#             return (rightmost_of_rc, lc, label, resulting_rc)
#
# T = ((None, "b", None), "a", (None, "c", None))
# print(popTree(T))


#maxElement
# def maxElement(T):
#     if T == None:
#         return None
#     else:
#         (lc, label, rc) = T
#         m = label
#         m_left = maxElement(lc)
#         m_right = maxElement(rc)
#         return max(m, m_left, m_right)


#sort binaryTree
# def isSorted(T, minBound = -30000, maxBound = 30000):
#     if T == None:
#         return True
#     else:
#         (lc, label, rc) = T
#         return (minBound <= label) and (label <= maxBound) and (isSorted(lc, minBound, label)) and (isSorted(rc, label, maxBound))
# T = (((None, 17, None), 35, None), 24, (((None, 61, None), 80, (None, 5, None))))
# T = (((None, 1, None), 2, (None, 2, None)), 3, (None, 4, (None, 5, None)))
# print(isSorted(T))

#List -> ordered binary tree
# class TreeNode:
#     def __int__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# def toSortedTree(X):
#     def level(index):
#         if index >= len(X) or X[index] is None:
#             return None
#
#         label = TreeNode(X[index])
#         label.left = level(2 * index + 1)
#         label.right = level(2 * index + 2)
#         return label
#
#     return level(0)
#
# X =  [3, 9, 20, None, None, 15, 7]
# tree = toSortedTree(X)

#printTree
# def printTree(T, indent = 0):
#     if T == None:
#         return " "
#     else:
#         (lc, l, rc) = T
#         result = "  " * indent + str(l) + '\n'
#         result += printTree(lc, indent=indent + 1)
#         result += printTree(rc, indent=indent + 1)
#         return result
#
# T = (((None, 17, None), 35, None), 24, (((None, 61, None), 80, (None, 5, None))))
# print(printTree(T))

#toSortedTree
def toSortedTree(X):
    if len(X) == 0:
        return None
    else:
        X_list = list(X)
        label = X_list[0]
        X_left, X_right = set(), set()
        for i in X_list[1:]:
            if i <= label:
                X_left.add(i)
            else:
                X_right.add(i)
        return (toSortedTree(X_left), label, toSortedTree(X_right))

