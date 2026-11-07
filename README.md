# Maths Toolkit 🧮

A robust, pure Python and NumPy-based Command-Line Interface (CLI) application designed to handle complex mathematical computations efficiently.
This toolkit consolidates three powerful modules: an Advanced Matrix Calculator, a Polynomial Root Solver, and a Statistical Analysis Engine into a single, interactive, and user-friendly menu.

## 🚀 Features

### 1. Advanced Matrix Calculator

*Performs 16 diverse linear algebra operations with strict validation for matrix dimensions and singularity:*

- **Basic Arithmetic:** Addition, Subtraction, Multiplication, and Scalar Multiplication.

- **Core Matrix Properties:** Transpose, Determinant, Trace, and Matrix Rank.

- **Advanced Computations:** Matrix Inversion, Matrix Powers, and Eigenvalues/Eigenvectors decomposition.

- **Error Handling:** Includes protections against dimension mismatch, non-square matrices for determinants/inverses, and singular matrix inversion.

### 2. Polynomial Solver

- Evaluates 1D numerical arrays to instantly compute foundational statistical metrics.

- Built-in validation to prevent division-by-zero errors (e.g., leading coefficient cannot be zero) and ensures the correct number of coefficient inputs.

### 3. Statistics Solver

- Evaluates 1D numerical arrays to instantly compute foundational statistical metrics.

- Calculates: Maximum, Minimum, Mean, Median, Mode, Variance, Standard Deviation, and Sum.

## 🛠️ Tech Stack

- **Language:** Python 3
  
- **Core Library:** NumPy (used for optimized array manipulations, linear algebra operations, and statistical calculations)
  
- **System Operations:** sys module for graceful application termination.

## 💻 How to Run (Installation & Execution)

**1. Clone the repository:**

git clone https://github.com/amit39underworld93-bot/MATHS_TOOLKIT.git cd MATHS_TOOLKIT

**2. Install dependencies (if not already installed):**

*This project requires `numpy` to execute matrix and statistical operations efficiently.*

`pip install numpy`

**3. Execute the script:**

`python3 1.py`

## 📸 Usage Overview

*When you launch the application, you will be greeted with the main interactive menu:*

===== MATHS TOOLKIT =====
1. Matrix solver
2. Polynomial solver
3. Statistics solver
4. Exit
Enter your choice:

***Simply type the number corresponding to your desired module, and the program will guide you through entering the data 
(e.g., matrix rows/columns, polynomial coefficients, or statistical arrays) step by step.***
