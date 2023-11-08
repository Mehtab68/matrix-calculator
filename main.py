def userInput():
    options = " 1. Add matrices \n 2. Multiply matrix by a constant \n 3. Multiply matrices \n 4. Transpose matrix \n 5. Calculate a determinant \n 6. Inverse Matrix \n 0. exit"
    print(options)
    choice = input("What operation would you like to choose : ")
    if choice == "1":
        size = input("Enter size of first matrix : ")
        createMatrix(size)
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


def createMatrix(size):
    row = int(size[0])
    column = int(size[2])
    i = 0
    while i < row:
        input("")
        i += 1


userInput()
