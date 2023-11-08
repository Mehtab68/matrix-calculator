def userInput():
    options = " 1. Add matrices \n 2. Multiply matrix by a constant \n 3. Multiply matrices \n 4. Transpose matrix \n 5. Calculate a determinant \n 6. Inverse Matrix \n 0. exit"
    print(options)
    choice = input("What operation would you like to choose : ")
    if choice == "1":
        size1 = input("Enter size of first matrix : ")
        addition(size1)
    elif choice == "2":
        return
    elif choice == "3":
        return
    elif choice == "4":
        return
    elif choice == "5":
        return
    elif choice == "6":
        return
    else:
        exit()


def addition(size1):
    Row = int(size1[0])
    Column = int(size1[2])

    # Initialize matrix
    matrix = []
    print("Enter the entries row wise:")

    # For user input
    # A for loop for row entries
    for row in range(Row):
        a = []
        # A for loop for column entries
        for column in range(Column):
            a.append(int(input()))
        matrix.append(a)

    size2 = input("Enter size of second matrix : ")
    Row1 = int(size2[0])
    Column1 = int(size2[2])

    # Initialize matrix
    matrix1 = []
    print("Enter the entries row wise:")

    # For user input
    # A for loop for row entries
    for row in range(Row1):
        a = []
        # A for loop for column entries
        for column in range(Column1):
            a.append(int(input()))
        matrix1.append(a)

    if Row == Row1 and Column == Column1:
        for row in range(Row):
            for column in range(Column):
                print(matrix[row][column] + matrix1[row][column], end=" ")
            print()
    else:
        print("Cannot add matrices together since it is not the same dimensions")


userInput()
