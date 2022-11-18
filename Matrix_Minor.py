
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


num_row1 = 3              #initialising the number of rows 
num_col1 = 3              #initialising the number of columns
print("enter the elements of 1st matrix")
mat1 = []                 # defining the matrix
for i in range(num_row1): # for loop to iterate between the rows of matrix
    a = []                # created a list to temproraly store the values
    for j in range(num_col1): # for loop to iterate between the columns of matrix
        q = int(input())  # taking input from the user
        a.append(q)       # storing the values to temporary list
    print()
    mat1.append(a)        # adding the elements to matrix
print("MATRIX-1")
for m in mat1:            # loop for printing the matrix
    print(m)  
Mat_Mnr = Matrix_Minor(mat1) # calling the function for finding the minor of matrix
print("\nMinor Matrix:")
for i in Mat_Mnr:          # printing the returned minor matrix
    print(i)

