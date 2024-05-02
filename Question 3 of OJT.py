#!/usr/bin/env python
# coding: utf-8

# # Assignment 

# # Question 3:Singular Value Decomposition (SVD): 
# Perform Singular Value Decomposition on the matrix A obtained in Question 2. Separate and print 
# matrices U, Σ, and 𝑉^T
# Verify that A equals the product of U, Σ, and 𝑉^T
# Additionally, find the rank 2 
# and rank 3 approximations of matrix A. 

# In[1]:


import numpy as np


# In[2]:


# Define the matrix A (use the A obtained from Question 2)
A = np.array([[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]])


# In[3]:


# Perform Singular Value Decomposition (SVD)
U, Sigma, V_transpose = np.linalg.svd(A)


# In[4]:


# Construct the diagonal matrix Sigma from the 1-D array Sigma
Sigma_mat = np.diag(Sigma)


# In[5]:


# Find the rank-2 approximation of matrix A
rank_2_approx = np.dot(U[:, :2], np.dot(np.diag(Sigma[:2]), V_transpose[:2, :]))
print("\nRank-2 Approximation of Matrix A:")
print(rank_2_approx)


# In[6]:


# Find the rank-3 approximation of matrix A
rank_3_approx = np.dot(U[:, :3], np.dot(np.diag(Sigma[:3]), V_transpose[:3, :]))
print("\nRank-3 Approximation of Matrix A:")
print(rank_3_approx)


# In[7]:


# Print matrices U, Sigma, and V_transpose
print("\nMatrix U:")
print(U)
print("\nMatrix Sigma:")
print(Sigma_mat)
print("\nMatrix V_transpose:")
print(V_transpose)


# In[ ]:




