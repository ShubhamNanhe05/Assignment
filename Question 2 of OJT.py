#!/usr/bin/env python
# coding: utf-8

# # Assignment

# # Question 2:  Row Echelon Form: 
# Create a 5x5 matrix, A, with entries randomly chosen integers between 0 and 9. To generate the 
# random matrix, set the random seed as the last two digits of your roll number. Reduce matrix A to its 
# Row Echelon Form by performing elementary row operations. 

# In[1]:


import numpy as np
np.random.seed(15)


# In[19]:


# Create a 5x5 matrix A with random integers between 0 and 9
A = np.random.randint(1, 5, size=(5, 5))
print("Matrix A:")
print(A)


# In[32]:


# Function to reduce matrix to row echelon form
def row_echelon_form(matrix):
    # Iterate over each row
    for i in range(len(matrix)):
        # Find the first non-zero element in the row
        pivot_index = -1
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                pivot_index = j
                break
 
  


# In[33]:


# Compute the row echelon form of matrix A
row_echelon_A = row_echelon_form(A.copy())
print("\nRow Echelon Form of Matrix A:")
print(row_echelon_A)


# In[ ]:





# In[ ]:




