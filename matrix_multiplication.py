#!/usr/bin/env python
# coding: utf-8

# In[1]:


num_row1 = int(input("enter the number of rows of 1st matrix:")) #entering the number of rows 
num_col1 = int(input('enter the number of columns of 1st matrix:')) #entering the number of columns
print("enter the elements of 1st matrix")
mat1 = [] # defining the matrix
for i in range(num_row1): #loop for entering the elements in matrix
    a = []
    for j in range(num_col1):
        w = int(input()) # entering the elements of matrix
        a.append(w)
    print()
    mat1.append(a) # adding the elements to matrix
print("MATRIX-1")
for m in mat1: # loop for printing the matrix
    print(m)  


# here we define a matrix (mat1) with num_row1 number of rows and num_col1 number of columns 
# we promt the user to enter the dimension of matrix and its elements 
# then we print the matrix-1

# In[2]:


num_row2 = int(input("enter the number of rows of 2nd matrix:")) #entering the number of rows 
num_col2 = int(input('enter the number of columns of 2nd matrix:')) # entering the number of columns
print("enter the elements of 2nd matrix")
mat2 = [] # defining the matrix
for i in range(num_row2): #loop for entering the elements in matrix
    a = []
    for j in range(num_col2):
        e = int(input()) # entering the elements of matrix
        a.append(e)
    print()
    mat2.append(a) # adding the elements to matrix
print("MATRIX-2")
for m in mat2: # loop for printing the matrix
    print(m)


# here we define a matrix (mat2) with num_row2 number of rows and num_col2 number of columns 
# we promt the user to enter the dimension of matrix and its elements 
# then we print the matrix-2

# In[3]:


if num_col1==num_row2: # checking if number of columns of 1st matrix is equal to number of rows of 2nd matrix
    result=[[0 for i in range(num_col2)] for j in range(num_row1)] # defining the result matrix
    for i in range(num_row1): # loop to iterating the rows of matrix 1
        for j in range(num_col2): # loop for iterating the columns of matrix 2
            for k in range(num_row2): # loop for iteratin the rows of matrix 2              
                result[i][j]+=int(mat1[i][k]*mat2[k][j]) # multiplying the elements and adding it to resultant matrix
    print("RESULT:")
    for r in result: # loop for printing the resultant matrix
        print(r)
else: # if number of columns of 1st matrix is not equal to number of rows of 2nd matrix 
    print("multiplication operation not possible")


#  checking if number of columns of 1st matrix is equal to number of rows of 2nd matrix 
#  defining the resultant matrix 
#  nested loop for multiplication process
#  multiplying the elements and adding it to the resultant matrix
#  printing the resultant matrix
#  printing "multiplication operation not possible" if number of columns of 1st matrix is not equal to number of rows of 2nd matrix 

# In[4]:


import numpy as np # importing numpy as np

res =  np.dot(mat1,mat2) # numpy function for multiplying 2 matrix
print("result by numpy")
print("RESULT:")
for r in res: # printing the result 
    print(r)


# In[ ]:




