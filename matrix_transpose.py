#!/usr/bin/env python
# coding: utf-8

# In[1]:


num_row1 = int(input("enter the number of rows of 1st matrix:")) #entering the number of rows 
num_col1 = int(input('enter the number of columns of 1st matrix:')) #entering the number of columns
print("enter the elements of 1st matrix")
mat = [] # defining the matrix
for i in range(num_row1): #loop for entering the elements in matrix
    a = []
    for j in range(num_col1):
        j = int(input()) # entering the elements of matrix
        a.append(j)
    print()
    mat.append(a) # adding the elements to matrix
print("MATRIX")
for m in mat: # loop for printing the matrix
    print(m)
    


# here we define a matrix  with num_row1 number of rows and num_col1 number of columns 
# we promt the user to enter the dimension of matrix and its elements 
# then we print the matrix

# In[2]:


tran_mat = [[0 for i in range(num_row1)] for j in range(num_col1)] # defining the transpose matrix 
for i in range(num_col1): #loop for transposing
    for j in range(num_row1):
        tran_mat[i][j]=mat[j][i] # performing the transpose operation 
for t in tran_mat:
    print(t) # printing the transpose matrix
        


# here we define a matrix (tran_mat) for the transposed matrix
# we inter change the values in column and rows
# print the resultent transposed matrix

# In[3]:


import numpy as np  # importing numpy as np
t_mat=np.transpose(mat) # numpy function for transposing a matrix
print("Result using numpy")
print("RESULT:")
for t in t_mat:
    print(t) # printing the result


# In[ ]:




