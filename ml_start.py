#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 07:35:16 2025

@author: robot
"""

import numpy as np 

# A = np.array([1,2,3])
# print(A.ndim)
# print(A.shape)

# B = np.zeros((3,2))
# print(type(B.shape))

# C = np.ones((3,4))
# print(C)
# print(C.size)

# D = np.full((2,3), 9)
# print(D)

# np.random.seed(0)
# print(np.random.randn(3,4))

# print(np.eye(4))

# print(np.linspace(0,10,20, dtype=np.float16))

# print(np.arange(0,10,0.5))

# E = np.zeros((3,2))
# F = np.ones((3,2))

# print(E)
# print(F)
# G = np.hstack((E,F))
# print(G)
# print(np.vstack((E,F)))
# H = np.concatenate((E,F), axis=1)
# print(H)
# print("H.shape:", H.shape)

def initialisation(m,n):
    return np.concatenate((np.random.randn(m,n),np.ones((m,1))), axis=1)


print(initialisation(3,4))