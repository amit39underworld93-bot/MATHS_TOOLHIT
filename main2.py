import numpy as np


# =========================================================
# MATRIX INPUT FUNCTION
# =========================================================

def input_matrix():

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []

    for i in range(rows):

        while True:

            row = list(map(int,input(f"Enter row {i + 1}: ").split()))

            if len(row) == cols:
                matrix.append(row)
                break

            print(f"Please enter exactly {cols} numbers.")

    return np.array(matrix)


# =========================================================
# MATRIX CALCULATOR
# =========================================================

def matrix_calculator():

    print("\n===== MATRIX CALCULATOR =====")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose of A")
    print("5. Transpose of B")
    print("6. Determinant of A")
    print("7. Determinant of B")
    print("8. Inverse of A")
    print("9. Inverse of B")
    print("10. Scalar multiplication of A")
    print("11. Scalar multiplication of B")
    print("12. Rank of A")
    print("13. Rank of B")
    print("14. Eigenvalues and Eigenvectors of A")
    print("15. Power of A")
    print("16. Power of B")

    choice = input("Enter your choice from 1 to 16: ")


    # =====================================================
    # ADDITION
    # =====================================================

    if choice == "1":

        print("\nEnter Matrix A:")
        A = input_matrix()

        print("\nEnter Matrix B:")
        B = input_matrix()

        if A.shape == B.shape:

            print("\nSum:")
            print(A + B)

        else:

            print("Error: Both matrices must have the same dimensions.")


    # =====================================================
    # SUBTRACTION
    # =====================================================

    elif choice == "2":

        print("\nEnter Matrix A:")
        A = input_matrix()

        print("\nEnter Matrix B:")
        B = input_matrix()

        if A.shape == B.shape:

            print("\nDifference:")
            print(A - B)

        else:

            print("Error: Both matrices must have the same dimensions.")


    # =====================================================
    # MULTIPLICATION
    # =====================================================

    elif choice == "3":

        print("\nEnter Matrix A:")
        A = input_matrix()

        print("\nEnter Matrix B:")
        B = input_matrix()

        if A.shape[1] == B.shape[0]:

            print("\nProduct:")
            print(A @ B)

        else:

            print(
                "Error: Number of columns of A "
                "must be equal to number of rows of B."
            )


    # =====================================================
    # TRANSPOSE A
    # =====================================================

    elif choice == "4":

        print("\nEnter Matrix A:")
        A = input_matrix()

        print("\nTranspose of A:")
        print(A.T)


    # =====================================================
    # TRANSPOSE B
    # =====================================================

    elif choice == "5":

        print("\nEnter Matrix B:")
        B = input_matrix()

        print("\nTranspose of B:")
        print(B.T)


    # =====================================================
    # DETERMINANT A
    # =====================================================

    elif choice == "6":

        print("\nEnter Matrix A:")
        A = input_matrix()

        if A.shape[0] == A.shape[1]:

            print("\nDeterminant of A:")
            print(np.linalg.det(A))

        else:

            print("Error: Determinant requires a square matrix.")


    # =====================================================
    # DETERMINANT B
    # =====================================================

    elif choice == "7":

        print("\nEnter Matrix B:")
        B = input_matrix()

        if B.shape[0] == B.shape[1]:

            print("\nDeterminant of B:")
            print(np.linalg.det(B))

        else:

            print("Error: Determinant requires a square matrix.")


    # =====================================================
    # INVERSE A
    # =====================================================

    elif choice == "8":

        print("\nEnter Matrix A:")
        A = input_matrix()

        if A.shape[0] != A.shape[1]:

            print("Error: Inverse requires a square matrix.")

        elif np.isclose(np.linalg.det(A), 0):

            print("Please enter a non-singular matrix!")

        else:

            print("\nInverse of A:")
            print(np.linalg.inv(A))


    # =====================================================
    # INVERSE B
    # =====================================================

    elif choice == "9":

        print("\nEnter Matrix B:")
        B = input_matrix()

        if B.shape[0] != B.shape[1]:

            print("Error: Inverse requires a square matrix.")

        elif np.isclose(np.linalg.det(B), 0):

            print("Please enter a non-singular matrix!")

        else:

            print("\nInverse of B:")
            print(np.linalg.inv(B))


    # =====================================================
    # SCALAR MULTIPLICATION A
    # =====================================================

    elif choice == "10":

        print("\nEnter Matrix A:")
        A = input_matrix()

        n = float(
            input("Enter the number to be multiplied with A: ")
        )

        print("\nResult:")
        print(A * n)


    # =====================================================
    # SCALAR MULTIPLICATION B
    # =====================================================

    elif choice == "11":

        print("\nEnter Matrix B:")
        B = input_matrix()

        n = float(
            input("Enter the number to be multiplied with B: ")
        )

        print("\nResult:")
        print(B * n)


    # =====================================================
    # RANK A
    # =====================================================

    elif choice == "12":

        print("\nEnter Matrix A:")
        A = input_matrix()

        print("\nMatrix A:")
        print(A)

        rank = np.linalg.matrix_rank(A)

        print("The rank of Matrix A is:")
        print(rank)


    # =====================================================
    # RANK B
    # =====================================================

    elif choice == "13":

        print("\nEnter Matrix B:")
        B = input_matrix()

        print("\nMatrix B:")
        print(B)

        rank = np.linalg.matrix_rank(B)

        print("The rank of Matrix B is:")
        print(rank)


    # =====================================================
    # EIGENVALUES AND EIGENVECTORS
    # =====================================================

    elif choice == "14":

        print("\nEnter Matrix A:")
        A = input_matrix()

        if A.shape[0] != A.shape[1]:

            print(
                "Error: Eigenvalues and eigenvectors "
                "require a square matrix."
            )

        else:

            eigenvalues, eigenvectors = np.linalg.eig(A)

            print("\nEigenvalues:")
            print(eigenvalues)

            print("\nEigenvectors:")
            print(eigenvectors)


    # =====================================================
    # POWER OF A
    # =====================================================

    elif choice == "15":

        print("\nEnter Matrix A:")
        A = input_matrix()

        if A.shape[0] != A.shape[1]:

            print("Matrix power requires a square matrix!!")

        else:

            n = int(input("Enter the power: "))

            print("Result:")
            print(np.linalg.matrix_power(A, n))


    # =====================================================
    # POWER OF B
    # =====================================================

    elif choice == "16":

        print("\nEnter Matrix B:")
        B = input_matrix()

        if B.shape[0] != B.shape[1]:

            print("Matrix power requires a square matrix!!")

        else:

            n = int(input("Enter the power: "))

            print("Result:")
            print(np.linalg.matrix_power(B, n))


    # =====================================================
    # INVALID MATRIX CHOICE
    # =====================================================

    else:

        print("\nSomething went wrong!")
        print("Please enter a number between 1 and 16.")


# =========================================================
# POLYNOMIAL SOLVER
# =========================================================

def polynomial_solver():

    degree = int(input("Enter a degree : "))

    # Degree 0
    if degree == 0:

        constant = float(input("Enter the constant: "))

        if constant == 0:

            print("Infinite solutions")

        else:

            print("No solutions")

        return


    # Take coefficients
    coefficients = list(map(float,input(f"Enter {degree + 1} coefficients : ").split()))


    # Check number of coefficients
    if len(coefficients) != degree + 1:

        print(f"Please enter exactly {degree + 1} coefficients.")
        return


    # Check leading coefficient
    if coefficients[0] == 0:

        print("Leading coefficient cannot be zero.")
        return


    # Find roots
    roots = np.roots(coefficients)


    print("\nROOTS ARE:")

    for i, root in enumerate(roots, start=1):

        print(f"x{i} = {root}")


# =========================================================
# STATISTICS SOLVER
# =========================================================

def statistics():

    print("\n =====STATISTICAL OPERATIONS=====")
    print("1. Max")
    print("2. Min")
    print("3. Standard deviation")
    print("4. Variance")
    print("5. Mean")
    print("6. Sum")
    print("7. Mode")
    print("8. Meadian")

    choice = input("Enter the choice: ")

    # MAXIMUM

    if choice == "1": 
        print("Enter the array: ")
        a = np.array(list(map(int, input("Enter numbers: ").split()))) 
        print(a)
        print("MAXIMUM: ", np.max(a))

    # MINIMUM
        
    elif choice == "2":
        print("Enter the array: ")
        a = np.array(list(map(int, input("Enter numbers: ").split()))) 
        print(a)
        print("MINIMUM: ", np.min(a))

    # STANDARD DEVIATION

    elif choice == "3":
        print("Enter the array: ")
        a = np.array(list(map(int, input("Enter numbers: ").split()))) 
        print(a)
        print("STANDARD DEVIATION: ", np.std(a))

    # VARIANCE

    elif choice == "4":
        print("Enter the array: ")
        a = np.array(list(map(int, input("Enter numbers: ").split()))) 
        print(a)
        print("VARIANCE: ", np.std(a))

    # MEAN

    elif choice == "5":
        print("Enter the array: ")
        a = np.array(list(map(int, input("Enter numbers: ").split()))) 
        print(a)
        print("MEAN: ", np.mean(a))

    # SUM

    elif choice == "6":
        print("Enter the array: ")
        a = np.array(list(map(int, input("Enter numbers: ").split()))) 
        print(a)
        print("SUM: ", np.sum(a))

    # MODE

    elif choice == "7":
        print("Enter the array: ")
        a = np.array(list(map(int, input("Enter numbers: ").split()))) 
        print(a)
        print("MODE: ", np.mode(a))

    # MEDIAN

    elif choice == "8":
        print("Enter the array: ")
        a = np.array(list(map(int, input("Enter numbers: ").split()))) 
        print(a)
        print("MEDIAN: ", np.median(a))


# =========================================================
# MAIN MENU
# =========================================================

def main_menu():

    print("\n===== MATHS TOOLKIT =====")

    print("1. Matrix solver")
    print("2. Polynomial solver")
    print("3. Statistics solver")

    choice = input("Enter your choice: ")


    if choice == "1":

        matrix_calculator()


    elif choice == "2":

        polynomial_solver()


    elif choice == "3":

        statistics()


    else:

        print("\nSomething went wrong!")
        print("Please enter a number between 1 and 3.")


# =========================================================
# START PROGRAM
# =========================================================

main_menu()