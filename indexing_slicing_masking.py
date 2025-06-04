#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 05:02:04 2025

@author: robot
"""

# import numpy as np

# A = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(A[1,1])
# print(A[0,:])
# print(A[0:2, 0:2])
# A[0:2, 0:2] = 10
# print(A)
# print(A[:,1:])
# print(A[:,-2:])

# B = np.zeros((4,4))

# print(B)
# B[1:3, 1:3] = 1
# print(B)
# C = np.zeros((5,5))
# C[::2,::2] = 1
# print(C)

# # Boolean Indexing
# A = np.random.randint(0,10,[5,5])
# print(A)
# A[(A<5) & (A > 2)] = 10
# print(A)

from scipy import misc
import matplotlib.pyplot  as plt 
face  = misc.face(gray=True)
plt.imshow(face)
print(face.shape)
