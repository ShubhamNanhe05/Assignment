#!/usr/bin/env python
# coding: utf-8

# # Assignment

# # Question 1:Data Visualization and Statistical Measures: 
# #For this question, you are required to analyse the iris dataset (iris.csv) using Python. Perform all 
# #possible data visualization techniques (histograms, scatter plots, box plots, etc.) on all numerical 
# #columns of the dataset. Additionally, calculate all possible statistical measures (mean, median, 
# #mode, standard deviation, etc.) for each numerical column. 
# 

# In[35]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[37]:


#Analyse the iris dataset
iris_df = pd.read_csv("F:\IMCA\OJT PRACTICALS\iris.csv")


# In[38]:


# Display the first few rows of the dataset
print(iris_df.head())


# In[39]:


# Summary statistics
summary_stats = iris_df.describe()
print(summary_stats)


# In[40]:


# Data visualization

# Histograms for numerical columns
iris_df.hist(figsize=(10, 8))
plt.suptitle("Histograms of Numerical Columns")
plt.show()


# In[41]:


# Box plots for numerical columns
iris_df.boxplot(figsize=(10, 8))
plt.title("Box Plots of Numerical Columns")
plt.show()


# In[42]:


# Pairplot for numerical columns
sns.pairplot(iris_df)
plt.suptitle("Pairplot of Numerical Columns")
plt.show()


# In[43]:


# Example data
data = [1, 2, 3, 4, 5]

# Create a pandas Series
series = pd.Series(data)

# Calculate mean using pandas
mean = series.mean()
print("Mean (pandas):", mean)


# In[44]:


# Calculate median using pandas
median = series.median()
print("Median:", median)


# In[45]:


# Calculate mode using pandas
mode = series.mode()
print("Mode:", mode[0]) # In case of multiple modes, the first one is returned


# In[46]:


# Calculate standard deviation using pandas
std_dev = series.std()
print("Standard Deviation:", std_dev)


# In[ ]:





# In[ ]:





# In[ ]:




