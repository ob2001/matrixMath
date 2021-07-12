# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 14:42:24 2021

@author: Obutler

- Functions for matrix operations on any matrices.
- These functions operate on instances of the matrix class
defined in UIFuncs.py
"""

import UIFuncs as ui
from UIFuncs import matrix

# This function is not accessible to the user.
# This is used in some functions such as adjugate()

# Transposes a matrix and adds the resulting matrix to the
# matrices list.
def initTranspose(matrices):
    matrixChoiceNum = ui.chooseMatrix(matrices, "Which matrix would you like to transpose? Enter 0 to exit this function: ")
    if(matrixChoiceNum == -1):
        return
    
    matrixChoice = matrices[matrixChoiceNum]
    
    # Transpose original matrix into new matrix
    newMatrix = transpose(matrixChoice)
    
    # Add transposed matrix and informatation to lists
    newMatrix = matrix(newMatrix, matrixChoice.cols, matrixChoice.rows)
    if(matrixChoice.label == ""):
        newMatrix.label = f"Transpose of matrix {matrixChoiceNum + 1}"
    else:
        newMatrix.label = f"Transpose of \"{matrixChoice.label}\""
    
    matrices.append(newMatrix)

    print(f"Transpose of matrix {matrixChoiceNum + 1}")
    ui.printMatrix(newMatrix)
    input("Press Enter to continue")
    return

def initAddMatrices(matrices):
    # Have user choose two matrices to add
    # User can enter 0 for either matrix to exit the function
    validChoice = 0
    while(not validChoice):
        matrixANum = ui.chooseMatrix(matrices, "Which matrices would you like to add? Enter 0 to exit this function (matrix A): ")
        if(matrixANum == -1):
            return
        matrixBNum = ui.chooseMatrix(matrices, "Which matrices would you like to add? Enter 0 to exit this function (matrix B): ")
        if(matrixBNum == -1):
            return
        if(matrices[matrixANum].rows != matrices[matrixBNum].rows or matrices[matrixANum].cols != matrices[matrixBNum].cols):
            print("Matrices must have same number of rows and columns.")
        else:
            validChoice = 1
            
    matrixA = matrices[matrixANum]
    matrixB = matrices[matrixBNum]
    
    newMatrix = addMatrices(matrixA, matrixB)
    
    if(matrixA.label == "" and matrixB.label == ""):
        print(f"Sum of matrix {matrixANum + 1} and matrix {matrixBNum + 1}")
        newMatrix.label = f"Sum of matrix {matrixANum + 1} and matrix {matrixBNum + 1}"
    elif(matrixB.label == ""):
        print(f"Sum of \"{matrixA.label}\" and matrix {matrixBNum + 1}")
        newMatrix.label = f"Sum of \"{matrixA.label}\" and matrix {matrixBNum + 1}"
    elif(matrixA.label == ""):
        print(f"Sum of matrix {matrixANum + 1} and \"{matrixB.label}\"")
        newMatrix.label = f"Sum of matrix {matrixANum + 1} and \"{matrixB.label}\""
    else:
        print(f"Sum of \"{matrixA.label}\" and \"{matrixB.label}\"")
        newMatrix.label = f"Sum of \"{matrixA.label}\" and \"{matrixB.label}\""
    ui.printMatrix(newMatrix)
    
    # Place the resulting matrix in the list of matrices
    matrices.append(newMatrix)
    input("Press Enter to continue")
    return

# Multiplies two matrices (of correct dimensions) and adds
# the resulting matrix to the matrices list.
def initMultiplyMatrices(matrices):
    validChoice = 0
    while(not validChoice):
        matrixANum = ui.chooseMatrix(matrices, "Which matrices would you like to multiply? Enter 0 to exit this function (matrix A): ")
        if(matrixANum == -1):
            return
        matrixBNum = ui.chooseMatrix(matrices, "Which matrices would you like to multiply? Enter 0 to exit this function (matrix B): ")
        if(matrixBNum == -1):
            return
        if(matrices[matrixANum].cols != matrices[matrixBNum].rows):
            print("The number of columns in Matrix A must be equal to the number of rows in Matrix B.")
        else:
            validChoice = 1
            
    matrixA = matrices[matrixANum]
    matrixB = matrices[matrixBNum]
    
    newMatrix = multiplyMatrices(matrixA, matrixB)
    
    if(matrixA.label == "" and matrixB.label == ""):
        print(f"Matrix product of matrix {matrixANum + 1} and matrix {matrixBNum + 1}")
        newMatrix.label = f"Matrix product of matrix {matrixANum + 1} and matrix {matrixBNum + 1}"
    elif(matrixB.label == ""):
        print(f"Matrix product of \"{matrixA.label}\" and matrix {matrixBNum + 1}")
        newMatrix.label = f"Matrix product of \"{matrixA.label}\" and matrix {matrixBNum + 1}"
    elif(matrixA.label == ""):
        print(f"Matrix product of matrix {matrixANum + 1} and \"{matrixB.label}\"")
        newMatrix.label = f"Matrix product of matrix {matrixANum + 1} and \"{matrixB.label}\""
    else:
        print(f"Matrix product of \"{matrixA.label}\" and \"{matrixB.label}\"")
        newMatrix.label = f"Matrix product of \"{matrixA.label}\" and \"{matrixB.label}\""
    
    print("Matrix product:")
    ui.printMatrix(newMatrix)
    matrices.append(newMatrix)
    input("Press Enter to continue")
    return

def initMatsEqual(matrices):
    matrixANum = ui.chooseMatrix(matrices, "Which matrices would you like to check the equality of? (matrix A): ")
    matrixBNum = ui.chooseMatrix(matrices, "Which matrices would you like to check the equality of? (matrix b): ")
    
    matrixA, matrixB = matrices[matrixANum], matrices[matrixBNum]
    
    equal = matsEqual(matrixA, matrixB)
    if(equal):
        print("The matrices are numerically equal.")
    else:
        print("The matrices are not numerically equal.")
    
    input("Press Enter to continue")
    return

def initAddRows(matrices):
    matrixChoiceNum = ui.chooseMatrix(matrices, "Which matrix would you like to perform the row operation on: ")
    
    row1 = ui.chooseRow(matrices[matrixChoiceNum], "Choose the row to be added to (row 1): ")
    if(row1 == -1):
        return
    row2 = ui.chooseRow(matrices[matrixChoiceNum], "Choose the row that will be added to row 1 (row 2): ")
    if(row2 == -1):
        return
    
    addRows(matrices[matrixChoiceNum], row1, row2)
    return

def initSwapRows(matrices):
    matrixChoiceNum = ui.chooseMatrix(matrices, "Which matrix would you like to perform the row operation on: ")
    
    row1 = ui.chooseRow(matrices[matrixChoiceNum], "Choose the first row to swap (row 1): ")
    if(row1 == -1):
        return
    row2 = ui.chooseRow(matrices[matrixChoiceNum], "Choose the second row to swap (row 2):")
    if(row2 == -1):
        return
    
    swapRows(matrices[matrixChoiceNum], row1, row2)
    return

def initMultiplyRow(matrices):
    matrixChoiceNum = ui.chooseMatrix(matrices, "Which matrix would you like to perform the row operation on: ")
    row = ui.chooseRow(matrices[matrixChoiceNum], "Which row would you like to multiply by a scalar: ")
    if(row == -1):
        return
    
    valid = False
    while(not valid):
        scalar = input("Input the scalar to multiply the row by: ")
        try:
            scalar = eval(scalar)
            valid = True
        except:
            print("Invalid scalar")
            
    multiplyRow(matrices[matrixChoiceNum], row, scalar)
    matrices[matrixChoiceNum].simplify
    return

def scalarMultiply(num, mat) -> matrix:
    newMatrix = [[0 for x in range(mat.rows)] for y in range(mat.cols)]
    for i in range(len(mat.mat)):
        for j in range(len(mat.mat[i])):
            newMatrix[i][j] = num * mat.mat[i][j]
    
    newMatrix = matrix(newMatrix, mat.rows, mat.cols)
    return newMatrix

# Returns the submatrix of a matrix given and entry
# to exclude.
def subMatrix(matrixChoice, excludedRow, excludedCol) -> matrix:
    tempMatrix = [[0 for x in range(matrixChoice.cols - 1)] for y in range(matrixChoice.cols - 1)]
    
    m, n = 0, 0
    for i in range(matrixChoice.cols):
        n = 0
        for j in range(matrixChoice.cols):
            if j == excludedCol:
                continue
            elif i == excludedRow:
                continue
            else:
                tempMatrix[m][n] = matrixChoice.mat[i][j]
                n += 1
        if i == excludedRow:
            continue
        else:
            m += 1
            
    newMatrix = matrix(tempMatrix, matrixChoice.rows - 1, matrixChoice.cols - 1)
    
    return newMatrix

def transpose(mat) -> matrix:
    tempMatrix = [[0 for x in range(mat.rows)] for y in range(mat.cols)]
    for i in range(mat.rows):
        for j in range(mat.cols):
            tempMatrix[j][i] = mat.mat[i][j]
            
    newMatrix = matrix(tempMatrix, mat.cols, mat.rows)
    return newMatrix

# Adds two matrices (of the same dimensions) and adds the 
# resulting matrix to the matrices list.
def addMatrices(mat1, mat2):
    # Add the matrices element-wise into a new matrix
    tempMatrix = [[0 for x in range(mat1.rows)] for y in range(mat2.cols)]
    for i in range(mat1.rows):
        for j in range(mat1.cols):
            tempMatrix[i][j] = mat1.mat[i][j] + mat2.mat[i][j]
            
    newMatrix = matrix(tempMatrix, mat1.rows, mat1.cols)
    return newMatrix

def multiplyMatrices(mat1, mat2) -> matrix:
    tempMatrix = [[0 for x in range(mat2.cols)] for y in range(mat1.rows)]
    for i in range(mat1.rows):
        for j in range(mat2.cols):
            for k in range(mat1.cols):
                tempMatrix[i][j] += mat1.mat[i][k] * mat2.mat[k][j]
    
    newMatrix = matrix(tempMatrix, mat1.rows, mat2.cols)
    newMatrix.simplify()
    return newMatrix

def matsEqual(mat1, mat2) -> bool:
    if(mat1.rows != mat2.rows or mat1.cols != mat2.cols):
        return False
    else:
        for i in range(len(mat1.mat)):
            for j in range(len(mat1.mat[i])):
                if(mat1.mat[i][j] != mat2.mat[i][i]):
                    return True
                else:
                    continue
    return True

def addRows(mat, row1, row2):
    for i in range(len(mat.mat[row1])):
        mat.mat[row1][i] += mat.mat[row2][i]
    return

def swapRows(mat, row1, row2):
    temp = mat.mat[row1]
    mat.mat[row1] = mat.mat[row2]
    mat.mat[row2] = temp
    return

def multiplyRow(mat, row, scalar):
    for i in range(len(mat.mat[row])):
        mat.mat[row][i] *= scalar
        
    mat.simplify()
    return