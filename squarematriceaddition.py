#program to perform addition of two square matrices

def getMatrix(n):  # creating the matrix
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(
                int(input("Enter element " + str(i) + "," + str(j) + ": ")))
    return matrix

def checkmatrixeligible():  # checking if the matrices are eligible for Addition or not
    n1_rows = int(input("Enter the number of rows in the first matrix: "))
    n1_cols = int(input("Enter the number of columns in the first matrix: "))
    n2_rows = int(input("Enter the number of rows in the Second matrix: "))
    n2_cols = int(input("Enter the number of columns in the Second matrix: "))
    if n1_cols == n2_rows == n2_cols == n1_rows:
        AddMatrix(n1_rows)
    else:
        print("\n\n Matrix Addition not possible because give matrix are not square matrices\n\n ")
        exit()

def displayMatrix(result):  # displaying the result
    print("\n\n The result of the Addition of Square Matrices is: \n\n")
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j], end=" ")
        print()

def AddMatrix(n):  # multiplication of two matrices
    matrix1 = getMatrix(n)
    matrix2 = getMatrix(n)
    result = []
    for i in range(len(matrix1)):
        sum=[]
        for j in range(len(matrix1[0])):
            sum.append(matrix1[i][j] + matrix2[i][j])
        result.append(sum)
    return displayMatrix(result)

checkmatrixeligible()