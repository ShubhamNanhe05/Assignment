#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sympy as sp
import numpy as np


# In[ ]:





# In[5]:


#from mmap import ACCESS_READ
from google.colab import files
from PIL import Image as Impil
from IPython.display import Image
uploaded = files.upload()
img = Impil.open(list(uploaded)[0])
display(pic)
imgGray = img.convert('L')
A = np.array(imgGray)
display(imgGray)


# In[ ]:




