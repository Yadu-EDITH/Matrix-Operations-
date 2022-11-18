import numpy as np          # importing numpy package as np
def Matrix_Minor(mat):      # function defifnition
    Lis=[]                  # created a list to  store the values of minor matrix
    for i in range(3):      # for loop to iterate between the rows of matrix
        for j in range(3):  # for loop to iterate between the columns of matrix
            Min_Lis1=[]     # created a list to temproraly store the values of minor of elements
            for k in range(3):   # for loop to iterate between the rows 
                for l in range(3):  # for loop to iterate between the columns
                    if (k!=i)&(l!=j):  # if condition to exclude the row elements and column elements
                                       # of the element which we are taking(eg: if we are taking the element
                                       # A11 then it will eleminate all the elements of row1 and column1)
                        Min_Lis1.append(mat[k][l]) # appending the rest 4 elements to the temporary list  
            q = Min_Lis1[0]*Min_Lis1[3]-Min_Lis1[1]*Min_Lis1[2] # calculating the value of minor matrix 
            Lis.append(q)    # appending the values of minor matrix to the list
    a=0        # valiable to iterate the elements of list
    res=[[0 for i in range(3)] for j in range(3)] # zero matrix for storing the values of minor matrix
    for i in range(3):    # for loop for iterating between the rows
        for j in range(3): # for loop for iterating between the columns
            res[i][j] = Lis[a]  # adding the values of minor matrix from list to matrix 
            a+=1   # updating the index value of list
    return res      # returning the minor matrix

def Cofactor_Matrix(cmat):     # defining the function to find the cofactor of the matrix
    Cof_Mat=[[0 for i in range(3)] for j in range(3)]    # zero matrix for storing the values of cofactor matrix
    for i in range(3):         # for loop to iterate between the rows
        for j in range(3):     # for loop to iterate between the columns
            if((i+j)%2!=0):    # if condition to check if the sum of i and j is odd
                Cof_Mat[i][j] = -1*cmat[i][j] # if true then multiply the cmat[i][j] element with -1 and add it to cofactor matrix 
            else: 
                Cof_Mat[i][j] = cmat[i][j] # else keep the same elements and add it to cofactor matrix
    return Cof_Mat   # return the cofactor matrix

def Adjoint_Matrix(amat):      # defining the function to find the adjoint of the matrix
    Adj_Mat = [[0 for i in range(3)] for j in range(3)] # zero matrix for storing the values of adjoint matrix 
    for i in range(3):         #loop for iterating between the rows
        for j in range(3):     # loop for iterating between the columns
            Adj_Mat[i][j]=amat[j][i] # performing the transpose operation to find the adjoint matrix 
    return Adj_Mat            # returning the adjoint matrix 

def Determinant_Matrix(dmat,cof):  # defining the function to find the determinant of the matrix
    d = 0                  # initialising the determinant to be zero
    for i in range(1):     # range of for loop is 1 as we only need to consider the first row of matrix
        for j in range(3): # for loop to iterate between the columns of 1st row
            d += dmat[i][j]*cof[i][j]  # updating the value of determinant 
    return d               #returning the determinant

def Inverse_Matrix(imat,d):       # defining a function to find the inverse of matrix
    Inv_Mat = [[0 for i in range(3)] for j in range(3)]   # zero matrix for storing the values of inverse of matrix 
    for i in range(3):           # for loop to iterate between the rows
        for j in range(3):       # for loop to iterate between the columns
            Inv_Mat[i][j] = imat[i][j]/d  # finding the inverse of matrix
    return Inv_Mat               # returning the inverse of matrix

num_row1 = 3              #initialising the number of rows 
num_col1 = 3              #initialising the number of columns
print("enter the elements of 1st matrix")
mat1 = []                 # defining the matrix
for i in range(num_row1): # for loop to iterate between the rows of matrix
    a = []                # created a list to temproraly store the values
    for j in range(num_col1): # for loop to iterate between the columns of matrix
        j = int(input())  # taking input from the user
        a.append(j)       # storing the values to temporary list
    print()
    mat1.append(a)        # adding the elements to matrix
print("MATRIX-1")
for m in mat1:            # loop for printing the matrix
    print(m)  
Mat_Mnr = Matrix_Minor(mat1) # calling the function for finding the minor of matrix
Mat_Cof = Cofactor_Matrix(Mat_Mnr) # calling the function for finding the cofactor matrix by passing the minor matrix 
Mat_Adj=Adjoint_Matrix(Mat_Cof) # calling the function for finding the adjoint matrix by passing the cofactor matrix
Mat_Det=Determinant_Matrix(mat1,Mat_Cof) # calling the function for finding the determinant of matrix by passing the initial matrix and cofactor matrix 
if Mat_Det==0:          # if determinant is zero then we cant find the inverse 
    print("Determinant is zero. Inverse operation is not possible") # if true exiting the program with a message 
else:                   # if false then proceding to find the inverse 
    Mat_Inv=Inverse_Matrix(Mat_Adj,Mat_Det) # calling the function to find the inverse 
    print("\nInverse of Matrix:") 
    for i in Mat_Inv:   # printing the value of inverse returned by the function
        print(i)
    print(" ")
    print("\nInverse of matrix using numpy:") 
    print(np.linalg.inv(mat1))    # printing the value of inverse using numpy package 
