
def Matrix_Functions(mat2):          # defining a function to call all the functions
    Mat_Mnr = Matrix_Minor(mat2)     # function call for minor matrix
    Mat_Cof = Cofactor_Matrix(Mat_Mnr) # function call for cofactor matrix
    Mat_Adj = Adjoint_Matrix(Mat_Cof)  # function call for adjoint matrix
    Mat_Det = Determinant_Matrix(mat2,Mat_Cof)  # function call for determinant of matrix
    return Mat_Det # returning the determinant



def Matrix_Minor(mat):      # function definition
    Lis=[]                  # created a list to  store the values of minor matrix
    for i in range(3):      # for loop to iterate between the rows of matrix
        for j in range(3):  # for loop to iterate between the columns of matrix
            Min_Lis1=[]     # created a list to temporarly  store the values of minor of elements
            for k in range(3):   # for loop to iterate between the rows 
                for l in range(3):  # for loop to iterate between the columns
                    if (k!=i)&(l!=j):  # if condition to exclude the row elements and column elements of the element which we are taking(eg: if we are taking the element A11 then it will eleminate all the elements of row1 and column1)  
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


def Cramers_Determinant(Mat):     # defining a function to calculate the determinants
    Const = [[0 for i in range(1)] for j in range(3)]  # zero matrix with 3*1 dimension
    for i in range(3):            # loop for iterating between the rows
        for j in range(1):        # loop for iterating between the columns
            Const[i][j]=Mat[i][3] # adding the values of constants from augmented matrix to constant matrix  
    a = 0                         # initializing the column numbers to be replaced  
    Det_Crm = [[0 for i in range(1)] for j in range(3)] # zero matrix with 3*1 dimension
    for i in range(3):            # loop for iterating between the rows
        for j in range(1):        # loop for iterating between the rows
            Det_Crm[i][j] = Replaced_Determinant(Const,Mat,a)  # calling the function to find the replaced determinant  and  adding it to the matrix
            a += 1                # updating the value of a so that the next column get replaced 
    return Det_Crm                # returning the matrix with determinants 


def Replaced_Determinant(const,mat,Col_Num):    # defining a function to find the determinant of the matrix after replacing the columns with constant values  
    temp = [[0 for i in range(3)] for j in range(3)] # zero matrix with 3*3 dimension 
    for i in range(3):          # for loop to iterate between the rows
        for j in range(3):      # for loop to iterate between the columns
            temp[i][j]=mat[i][j]  # created a temporary matrix with the same values of initial matrix 
    for i in range(3):          # for loop to iterate between the rows
        for j in range(3):      # for loop to iterate between the columns
            if j == Col_Num:    # checking if column number is same as the passed value 
                temp[i][j]=const[i][0]  # if true then I replace that column with the constant values
            else:
                temp[i][j]=temp[i][j]   # if false then the column values remain the same 
    Det_R = Matrix_Functions(temp)      # call the function to find the determinant of updated temporary matrix 
    return Det_R                # returning the determinant


def Equation_Solution_Cramers(Rep,Det):     # defining a function to find the solution
    Sol = [[0 for i in range(1)] for j in range(3)] # created a 0 matrix with dimension 3*1
    for i in range(3):          # for loop to iterate between the rows
        for j in range(1):      # for loop to iterate between the columns
            Sol[i][j] =Rep[i][j]/Det     # finding the solution from replaced_determinant and determinant
    return Sol                  # returning the solution matrix


num_row1 = 3              #initialising the number of rows 
num_col1 = 4              #initialising the number of columns
print("enter the elements of the augmented matrix")
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
mat_det = Matrix_Functions(mat1)  # calling teh function to find the determinant of the matrix 
if mat_det==0:            # checking if determinant is zero then we cant find the solution
    print("Determinant is zero. Solution cannot be found ") # if true exiting the program with
else:                     # if false then proceed  
    print(" ")
    Crm_Det = Cramers_Determinant(mat1)      # calling the function to find the determinant after replacing the columns with constants
    Eqn_Sol = Equation_Solution_Cramers(Crm_Det,mat_det)  #calling the function to find teh solution
    print("Solution using Cramers rule:")    # printing the solution 
    print("X = "+ str(Eqn_Sol[0][0]))
    print("Y = "+ str(Eqn_Sol[1][0]))
    print("Z = "+ str(Eqn_Sol[2][0]))
