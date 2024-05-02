#!/usr/bin/env python
# coding: utf-8

# # Assignment 

# # Question 4:Polynomial Plotting with Annotations: 
# Randomly select the coefficients of a 5th degree polynomial. Set the random seed as the last two 
# digits of your roll number. Plot the polynomial for -5 ≤ x ≤ 5. Annotate the plot to identify the 
# maxima and minima of the polynomial. 

# In[30]:


import numpy as np
import matplotlib.pyplot as plt
np.random.seed(15)


# In[31]:


coff = np.random.randint(0,15,7)
X = np.arange(-5,5+0.1,0.1)
Y = coff[1]*(X**5) + coff[2]*(X**4) + coff[3]*(X**3) +coff[4]*(X**2) + coff[5]*(X) +coff[6]
plt.plot(X,Y, color='purple')
plt.xlabel('X')
plt.ylabel('Y')

plt.annotate("maxima",xy=(5,80000))
plt.annotate("minima",xy=(0,0))
plt.show()


# In[ ]:





# In[ ]:




