import numpy as np
import sys

# =========================================================
# MATRIX INPUT FUNCTION
# =========================================================

def input_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []

    for i in range(rows):
        while True:
            row = list(map(int,input(f"Enter row {i + 1} (space separated): ").split()))
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

    choice = input("Enter the choice between 1 to 16: ").strip()

    valid_choices = [str(i) for i in range(1, 17)]
    if choice not in valid_choices:
        print("Please enter a valid choice between 1 to 16.")
        return 

    # ADDITION
    if choice == "1":
        print("\nEnter Matrix A:")
        A = input_matrix()
        print("\nEnter Matrix B:")
        B = input_matrix()
        if A.shape == B.shape:
            print("\nSum:\n", A + B)
        else:
            print("Error: Both matrices must have the same dimensions.")

    # SUBTRACTION
    elif choice == "2":
        print("\nEnter Matrix A:")
        A = input_matrix()
        print("\nEnter Matrix B:")
        B = input_matrix()
        if A.shape == B.shape:
            print("\nDifference:\n", A - B)
        else:
            print("Error: Both matrices must have the same dimensions.")

    # MULTIPLICATION
    elif choice == "3":
        print("\nEnter Matrix A:")
        A = input_matrix()
        print("\nEnter Matrix B:")
        B = input_matrix()
        if A.shape[1] == B.shape[0]:
            print("\nProduct:\n", A @ B)
        else:
            print("Error: Number of columns of A must be equal to number of rows of B.")

    # TRANSPOSE A
    elif choice == "4":
        print("\nEnter Matrix A:")
        A = input_matrix()
        print("\nTranspose of A:\n", A.T)

    # TRANSPOSE B
    elif choice == "5":
        print("\nEnter Matrix B:")
        B = input_matrix()
        print("\nTranspose of B:\n", B.T)

    # DETERMINANT A
    elif choice == "6":
        print("\nEnter Matrix A:")
        A = input_matrix()
        if A.shape[0] == A.shape[1]:
            print("\nDeterminant of A:\n", np.linalg.det(A))
        else:
            print("Error: Determinant requires a square matrix.")

    # DETERMINANT B
    elif choice == "7":
        print("\nEnter Matrix B:")
        B = input_matrix()
        if B.shape[0] == B.shape[1]:
            print("\nDeterminant of B:\n", np.linalg.det(B))
        else:
            print("Error: Determinant requires a square matrix.")

    # INVERSE A
    elif choice == "8":
        print("\nEnter Matrix A:")
        A = input_matrix()
        if A.shape[0] != A.shape[1]:
            print("Error: Inverse requires a square matrix.")
        elif np.isclose(np.linalg.det(A), 0):
            print("Error: Please enter a non-singular matrix (Determinant shouldn't be 0).")
        else:
            print("\nInverse of A:\n", np.linalg.inv(A))

    # INVERSE B
    elif choice == "9":
        print("\nEnter Matrix B:")
        B = input_matrix()
        if B.shape[0] != B.shape[1]:
            print("Error: Inverse requires a square matrix.")
        elif np.isclose(np.linalg.det(B), 0):
            print("Error: Please enter a non-singular matrix (Determinant shouldn't be 0).")
        else:
            print("\nInverse of B:\n", np.linalg.inv(B))

    # SCALAR MULTIPLICATION A
    elif choice == "10":
        print("\nEnter Matrix A:")
        A = input_matrix()
        n = float(input("Enter the number to be multiplied with A: "))
        print("\nResult:\n", A * n)

    # SCALAR MULTIPLICATION B
    elif choice == "11":
        print("\nEnter Matrix B:")
        B = input_matrix()
        n = float(input("Enter the number to be multiplied with B: "))
        print("\nResult:\n", B * n)

    # RANK A
    elif choice == "12":
        print("\nEnter Matrix A:")
        A = input_matrix()
        print("The rank of Matrix A is:\n", np.linalg.matrix_rank(A))

    # RANK B
    elif choice == "13":
        print("\nEnter Matrix B:")
        B = input_matrix()
        print("The rank of Matrix B is:\n", np.linalg.matrix_rank(B))

    # EIGENVALUES AND EIGENVECTORS
    elif choice == "14":
        print("\nEnter Matrix A:")
        A = input_matrix()
        if A.shape[0] != A.shape[1]:
            print("Error: Eigenvalues and eigenvectors require a square matrix.")
        else:
            eigenvalues, eigenvectors = np.linalg.eig(A)
            print("\nEigenvalues:\n", eigenvalues)
            print("\nEigenvectors:\n", eigenvectors)

    # POWER OF A
    elif choice == "15":
        print("\nEnter Matrix A:")
        A = input_matrix()
        if A.shape[0] != A.shape[1]:
            print("Matrix power requires a square matrix!!")
        else:
            n = int(input("Enter the power: "))
            print("Result:\n", np.linalg.matrix_power(A, n))

    # POWER OF B
    elif choice == "16":
        print("\nEnter Matrix B:")
        B = input_matrix()
        if B.shape[0] != B.shape[1]:
            print("Matrix power requires a square matrix!!")
        else:
            n = int(input("Enter the power: "))
            print("Result:\n", np.linalg.matrix_power(B, n))


# =========================================================
# POLYNOMIAL SOLVER
# =========================================================

def polynomial_solver():
    degree = int(input("Enter the degree: "))
    if degree == 0:
        constant = float(input("Enter the constant: "))
        if constant == 0:
            print("Infinite solutions")
        else:
            print("No solutions")
        return

    coefficients = list(map(float,input(f"Enter {degree + 1} coefficients separated by space: ").split()))
    
    if len(coefficients) != degree + 1:
        print(f"Please enter exactly {degree + 1} coefficients.")
        return

    if coefficients[0] == 0:
        print("Leading coefficient cannot be zero.")
        return

    roots = np.roots(coefficients)
    print("\nROOTS ARE:")
    for i, root in enumerate(roots, start=1):
        print(f"x{i} = {root}")


# =========================================================
# STATISTICS SOLVER
# =========================================================

def statistics():
    print("\n===== STATISTICAL OPERATIONS =====")
    print("1. Max\n2. Min\n3. Standard deviation\n4. Variance")
    print("5. Mean\n6. Sum\n7. Mode\n8. Median")

    choice = input("Enter the choice: ").strip()
    
    if choice not in [str(i) for i in range(1, 9)]:
        print("Invalid choice!")
        return

    try:
        a = np.array(list(map(float, input("Enter numbers separated by space: ").split()))) 
        print("\nArray:", a)
    except ValueError:
        print("Please enter valid numbers only.")
        return

    if choice == "1": 
        print("MAXIMUM: ", np.max(a))
    elif choice == "2":
        print("MINIMUM: ", np.min(a))
    elif choice == "3":
        print("STANDARD DEVIATION: ", np.std(a))
    elif choice == "4":
        print("VARIANCE: ", np.var(a))
    elif choice == "5":
        print("MEAN: ", np.mean(a))
    elif choice == "6":
        print("SUM: ", np.sum(a))
    elif choice == "7":
        vals, counts = np.unique(a, return_counts=True)
        mode_val = vals[np.argmax(counts)]
        print("MODE: ", mode_val)
    elif choice == "8":
        print("MEDIAN: ", np.median(a))


# =========================================================
# MAIN MENU
# =========================================================

def main_menu():
    while True:
        print("\n===== MATHS TOOLKIT =====")
        print("1. Matrix solver")
        print("2. Polynomial solver")
        print("3. Statistics solver")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            matrix_calculator()
        elif choice == "2":
            polynomial_solver()
        elif choice == "3":
            statistics()
        elif choice == "4":
            print("Exiting toolkit...")
            sys.exit()
        else:
            print("\nSomething went wrong! Please enter a valid choice between 1 and 4.")

# =========================================================
# START PROGRAM
# =========================================================

main_menu()