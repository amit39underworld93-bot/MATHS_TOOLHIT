import numpy as np

def matrix():

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []

    for i in range(rows):

        while True:

            row = list(
                map(
                    int,
                    input(f"Enter row {i + 1}: ").split()
                )
            )

            if len(row) == cols:
                matrix.append(row)
                break

            print(f"Please enter exactly {cols} numbers.")

    return np.array(matrix)


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


# ---------------- ADDITION ----------------

if choice == "1":

    print("\nEnter Matrix A:")
    A = matrix()

    print("\nEnter Matrix B:")
    B = matrix()

    if A.shape == B.shape:

        print("\nSum:")
        print(A + B)

    else:

        print("Error: Both matrices must have the same dimensions.")


# ---------------- SUBTRACTION ----------------

elif choice == "2":

    print("\nEnter Matrix A:")
    A = matrix()

    print("\nEnter Matrix B:")
    B = matrix()

    if A.shape == B.shape:

        print("\nDifference:")
        print(A - B)

    else:

        print("Error: Both matrices must have the same dimensions.")


# ---------------- MULTIPLICATION ----------------

elif choice == "3":

    print("\nEnter Matrix A:")
    A = matrix()

    print("\nEnter Matrix B:")
    B = matrix()

    if A.shape[1] == B.shape[0]:

        print("\nProduct:")
        print(A @ B)

    else:

        print(
            "Error: Number of columns of A "
            "must be equal to number of rows of B."
        )


# ---------------- TRANSPOSE A ----------------

elif choice == "4":

    print("\nEnter Matrix A:")
    A = matrix()

    print("\nTranspose of A:")
    print(A.T)


# ---------------- TRANSPOSE B ----------------

elif choice == "5":

    print("\nEnter Matrix B:")
    B = matrix()

    print("\nTranspose of B:")
    print(B.T)


# ---------------- DETERMINANT A ----------------

elif choice == "6":

    print("\nEnter Matrix A:")
    A = matrix()

    if A.shape[0] == A.shape[1]:

        print("\nDeterminant of A:")
        print(np.linalg.det(A))

    else:

        print("Error: Determinant requires a square matrix.")


# ---------------- DETERMINANT B ----------------

elif choice == "7":

    print("\nEnter Matrix B:")
    B = matrix()

    if B.shape[0] == B.shape[1]:

        print("\nDeterminant of B:")
        print(np.linalg.det(B))

    else:

        print("Error: Determinant requires a square matrix.")


# ---------------- INVERSE A ----------------

elif choice == "8":

    print("\nEnter Matrix A:")
    A = matrix()

    if A.shape[0] != A.shape[1]:

        print("Error: Inverse requires a square matrix.")

    elif np.isclose(np.linalg.det(A), 0):

        print("Please enter a non-singular matrix!")

    else:

        print("\nInverse of A:")
        print(np.linalg.inv(A))


# ---------------- INVERSE B ----------------

elif choice == "9":

    print("\nEnter Matrix B:")
    B = matrix()

    if B.shape[0] != B.shape[1]:

        print("Error: Inverse requires a square matrix.")

    elif np.isclose(np.linalg.det(B), 0):

        print("Please enter a non-singular matrix!")

    else:

        print("\nInverse of B:")
        print(np.linalg.inv(B))


# ---------------- SCALAR MULTIPLICATION A ----------------

elif choice == "10":

    print("\nEnter Matrix A:")
    A = matrix()

    n = float(
        input("Enter the number to be multiplied with A: ")
    )

    print("\nResult:")
    print(A * n)


# ---------------- SCALAR MULTIPLICATION B ----------------

elif choice == "11":

    print("\nEnter Matrix B:")
    B = matrix()

    n = float(
        input("Enter the number to be multiplied with B: ")
    )

    print("\nResult:")
    print(B * n)


# ---------------- RANK A ----------------

elif choice == "12":

    print("\nEnter Matrix A:")
    A = matrix()

    print("\nMatrix A:")
    print(A)

    rank = np.linalg.matrix_rank(A)

    print("The rank of Matrix A is:")
    print(rank)


# ---------------- RANK B ----------------

elif choice == "13":

    print("\nEnter Matrix B:")
    B = matrix()

    print("\nMatrix B:")
    print(B)

    rank = np.linalg.matrix_rank(B)

    print("The rank of Matrix B is:")
    print(rank)


# ---------------- EIGENVALUES & EIGENVECTORS ----------------

elif choice == "14":

    print("\nEnter Matrix A:")
    A = matrix()

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

# -------------------- POWER OF A---------------------

elif choice == "15":
    print("\n Enter Matrix A:")
    A = matrix()
    if A.shape[0] != A.shape[1]:
        print("Matrix power requires a square matrix!!")

    else:
        n = int(input("Enter the power: "))
        print("result: ")
        print(np.linalg.matrix_power(A, n))

# -------------------- POWER OF B---------------------

elif choice == "16":
    print("\n Enter Matrix B:")
    B = matrix()
    if B.shape[0] != B.shape[1]:
        print("Matrix power requires a square matrix!!")

    else:
        n = int(input("Enter the power: "))
        print("result: ")
        print(np.linalg.matrix_power(B, n))

# ---------------- INVALID CHOICE ----------------



else:

    print("\nSomething went wrong!")
    print("Please enter a number between 1 and 16.")







def polynomial_solver():

    degree = int(input("Enter a degree: "))

    if degree == 0:
        constant = float(input("Enter the constant: "))

        if constant ==0:
            print("infinite solutions")

        else:
            print("no solutions")

            return

    coefficients = list(map(float, input(f"Enter {degree+1} coefficients: ").split()))

    if len(coefficients) != degree + 1:
        print(f"please enter {degree + 1} coefficients")

    if coefficients[0] == 0:
        print("leading coefficients cannot be zero")

    roots = np.roots(coefficients)

    print("ROOTS ARE: ", roots)



# polynomial_solver()


def main_menu():

    

        print("=====MATHS TOOLKIT=====")

        print("1. Mtrix solver")
        print("2. Polynomial solver")
        print("3. Statistics solver")

choice = input("Enter your choice: ")

if choice == "1":

    matrix()

elif choice == "2":

    polynomial_solver()

elif choice == "3":
    print("end of program")
    

else:

    print("\nSomething went wrong!")
    print("Please enter a number between 1 and 3.")

main_menu()