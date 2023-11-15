import numpy as np
import sys


def userInput():
    options = " 1. Add matrices \n 2. Multiply matrix by a constant \n 3. Multiply matrices \n 4. Transpose matrix \n 5. Calculate a determinant \n 6. Inverse Matrix  \n 7. Substract Matrix  \n 0. exit"
    print(options)
    choice = input("What operation would you like to choose : ")
    if choice == "1":
        size1 = input("Enter size of first matrix : ")
        matrix = []
        createMatrix(size1, matrix)
        size2 = input("Enter size of second matrix : ")
        matrix1 = []
        createMatrix(size2, matrix1)
        addition(size1, size2, matrix, matrix1)
    elif choice == "2":
        size1 = input("Enter the size of the matrix : ")
        constant = input("Enter the constant multiplicated : ")
        matrix = []
        createMatrix(size1, matrix)
        constantMultiplication(size1, matrix, constant)
    elif choice == "3":
        size1 = input("Enter size of first matrix : ")
        matrix = []
        createMatrix(size1, matrix)
        size2 = input("Enter size of second matrix : ")
        matrix1 = []
        createMatrix(size2, matrix1)
        matriceMultiplication(size1, size2, matrix, matrix1)
    elif choice == "4":
        size1 = input("Enter the size of the matrix : ")
        matrix = []
        createMatrix(size1, matrix)
        transpose(size1, matrix)
    elif choice == "5":
        size1 = input("Enter the size of the matrix : ")
        matrix = []
        createMatrix(size1, matrix)
        determinant(size1, matrix)
    elif choice == "6":
        return
    elif choice == "7":
        size1 = input("Enter size of first matrix : ")
        matrix = []
        createMatrix(size1, matrix)
        size2 = input("Enter size of second matrix : ")
        matrix1 = []
        createMatrix(size2, matrix1)
        substract(size1, size2, matrix, matrix1)
    else:
        exit()


def addition(size1, size2, matrix, matrix1):
    Row = int(size1[0])
    Column = int(size1[2])

    Row1 = int(size2[0])
    Column1 = int(size2[2])

    if Row == Row1 and Column == Column1:
        for row in range(Row):
            for column in range(Column):
                print(matrix[row][column] + matrix1[row][column], end=" ")
            print()
    else:
        print("Cannot add matrices together since it is not the same dimensions")


def substract(size1, size2, matrix, matrix1):
    Row = int(size1[0])
    Column = int(size1[2])

    Row1 = int(size2[0])
    Column1 = int(size2[2])

    if Row == Row1 and Column == Column1:
        for row in range(Row):
            for column in range(Column):
                print(matrix[row][column] - matrix1[row][column], end=" ")
            print()
    else:
        print("Cannot add matrices together since it is not the same dimensions")


def constantMultiplication(size1, matrix, constant):
    Row = int(size1[0])
    Column = int(size1[2])
    Constant = int(constant[0])

    for row in range(Row):
        for column in range(Column):
            print(matrix[row][column] * Constant, end=" ")
        print()


def transpose(size1, matrix):
    Row = int(size1[0])
    Column = int(size1[2])

    arr = np.array(matrix)

    arr_tranpose = arr.transpose()

    print(arr_tranpose)


def matriceMultiplication(size1, size2, matrix, matrix1):
    Row = int(size1[0])
    Column = int(size1[2])

    Row1 = int(size2[0])
    Column1 = int(size2[2])

    if Column != Row1:
        print("The operation cannot be performed.")

    result = []

    for i in range(Row):
        a = []
        for j in range(Column1):
            a.append(0)
        result.append(a)

    for i in range(len(matrix)):
        for j in range(len(matrix1)):
            for k in range(len(matrix1)):
                result[i][j] += matrix[i][k] * matrix1[k][j]

    for r in result:
        print(r)


def determinant(size1, matrix):
    Row = int(size1[0])
    Column = int(size1[2])

    if Row != Column:
        ("The determinant cannot be calculated")
    elif Row and Column == 1:
        determinant = matrix[0][0]
        print("The determinant of this matrix is " + str(determinant))
    elif Row and Column == 2:
        determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        print("The determinant of this matrix is " + str(determinant))
    else:
        i = 0
        for entry in matrix[i]:
            for j in range(1, len(matrix)):
                for k in range(1, len(matrix)):
                    print(matrix[j][k])


def createMatrix(size1, matrix):
    Row = int(size1[0])
    Column = int(size1[2])

    # Initialize matrix

    print("Enter the entries row wise:")

    # For user input
    # A for loop for row entries
    for row in range(Row):
        a = []
        # A for loop for column entries
        for column in range(Column):
            a.append(int(input()))
        matrix.append(a)

    return matrix


userInput()
