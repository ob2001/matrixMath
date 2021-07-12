# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 14:42:37 2021

@author: Obutler

- Functions for matrix operations on square matrices
- These functions operate on instances of the matrix class
deined in UIFuncs.py
"""

import UIFuncs as ui
import matFuncs as matf
from UIFuncs import matrix

# Wraps the functionality of det(), allowing for the user to
# choose a matrix. The determinant is not saved by the
# calculator because it is a scalar.
def initDet(matrices):
    validChoice = 0
    while(not validChoice):
        matrixChoiceNum = ui.chooseMatrix(matrices, "Which matrix would you like to take the determinant of? Enter 0 to exit this function: ")
        if(matrixChoiceNum == -1):
            return
        if(matrices[matrixChoiceNum].rows != matrices[matrixChoiceNum].cols):
            print("Matrix must be square")
        else:
            validChoice = 1
            
    matrixChoice = matrices[matrixChoiceNum]
    
    result = det(matrixChoice)
    if(matrixChoice.label == ""):
        print(f"Determinant of matrix {matrixChoiceNum + 1}: {result}")
    else:
        print(f"Determinant of matrix {matrixChoiceNum + 1} ({matrixChoice.label}): {result}")
        
    input("Press Enter to continue")
    return

# Called by initDet() for recursion.
# Does not handle choosing a matrix to take
# the determinant of.
def det(matrixChoice) -> int:
    result = 0
    if(matrixChoice.cols > 2):
        for i in range(matrixChoice.cols):
            result += ((-1)**i)*matrixChoice.mat[0][i]*det(matf.subMatrix(matrixChoice, 0, i))
    else:
        result += matrixChoice.mat[0][0] * matrixChoice.mat[1][1] - matrixChoice.mat[0][1] * matrixChoice.mat[1][0]
    
    return result

# Calculates and prints the trace of a matrix.
# The trace is not saved by the calculator
# because it is a scalar.
def trace(matrices):
    validChoice = 0
    while(not validChoice):
        matrixChoiceNum = input("Which matrix would you like to find the trace of? Enter 0 to exit this function: ")
        if matrixChoiceNum.isnumeric():
            matrixChoiceNum = int(matrixChoiceNum) - 1
            if(matrixChoiceNum == -1):
                return
            elif(matrixChoiceNum < -1 or matrixChoiceNum > len(matrices) - 1):
                print("Invalid matrix choice")
            elif(matrices[matrixChoiceNum].rows != matrices[matrixChoiceNum].cols):
                print("Matrix must be square")
            else:
                validChoice = 1
        else:
            print("Invalid matrix choice")    
    
    matrixChoice = matrices[matrixChoiceNum]
    result = 0
    for i in range(matrixChoice.cols):
        result += matrixChoice.mat[i][i]
        
    if(matrixChoice.label == ""):
        print(f"Trace: {result}")
    else:
        print(f"Trace of matrix {matrixChoiceNum + 1} ({matrixChoice.label}): {result}")
        
    input("Press Enter to continue")
    return

# Calculates the inverse of a matrix and adds the resulting
# matrix to the matrices list
def invertMatrix(matrices):
    matrixChoiceNum = ui.chooseMatrix(matrices, "Which matrix would you like to invert? Enter 0 to exit this function: ")
    if(matrixChoiceNum == -1):
        return
    
    matrixChoice = matrices[matrixChoiceNum]
    if(det(matrixChoice) == 0):
        print("Error - matrix not invertible; rows not linearly independent")
        return
    
    newMatrix = matf.scalarMultiply(1/det(matrixChoice), adjugate(matrixChoice))
    newMatrix.simplify()
    
    if(matrixChoice.label == ""):
        newMatrix.label = f"Inverse of matrix {matrixChoiceNum + 1}"
    else:
        newMatrix.label = f"Inverse of \"{matrixChoice.label}\""
    
    print("Inverse of matrix:")
    ui.printMatrix(newMatrix)
    
    matrices.append(newMatrix)
    input("Press Enter to continue")
    return

# Wraps the functionality of adjugate(), allowing for
# the user to choose a matrix. The resulting adjugate
# matrix is added to the matrices list.
def initAdjugate(matrices):
    matrixChoiceNum = ui.chooseMatrix(matrices, "Which matrix would you like to find the adjugate of? Enter 0 to exit this function: ")
    if(matrixChoiceNum == -1):
        return
    
    matrixChoice = matrices[matrixChoiceNum]
    newMatrix = adjugate(matrixChoice)
    
    if(matrixChoice.label == ""):
        newMatrix.label = f"Adjugate of matrix {matrixChoiceNum + 1}"
    else:
        newMatrix.label = f"Adjugate of \"{matrixChoice.label}\""
    
    print("Adjugate of matrix:")
    ui.printMatrix(newMatrix)
    
    matrices.append(newMatrix)
    input("Press Enter to continue")
    return

# Called by initAdjugate() for recursion.
# Does not handle choosing a matrix to find the
# adjugate matrix of.
def adjugate(matrixChoice) -> matrix:
    tempMatrix = []
    tempRow = []
    
    if(matrixChoice.cols == 2):
        tempMatrix = [[matrixChoice.mat[1][1], -matrixChoice.mat[0][1]], [-matrixChoice.mat[1][0], matrixChoice.mat[0][0]]]
        
    else:
        for i in range(len(matrixChoice.mat)):
            tempRow = []
            for j in range(len(matrixChoice.mat[i])):
                tempRow.append((-1)**(i + j)*det(matf.subMatrix(matrixChoice, i, j)))
            tempMatrix.append(tempRow)
    
    newMatrix = matrix(tempMatrix, matrixChoice.rows, matrixChoice.cols)
    newMatrix = matf.transpose(newMatrix)
    
    newMatrix.simplify()
    
    return newMatrix

def initMatsCommute(matrices):
    matrixANum = ui.chooseMatrix(matrices, "Which matrices would you like to check the commutivity of? (matrixA): ")
    matrixBNum = ui.chooseMatrix(matrices, "Which matrices would you like to check the commutivity of? (matrixB): ")
    
    matrixA, matrixB = matrices[matrixANum], matrices[matrixBNum]
    
    if(matsCommute(matrixA, matrixB)):
        print("Matrices commute.")
    else:
        print("Matrices do not commute.")
        
    input("Press Enter to continue")
    return

def matsCommute(mat1, mat2) -> bool:
    prod1 = matf.multiplyMatrices(mat1, mat2)
    prod2 = matf.multiplyMatrices(mat2, mat1)
    
    if(matf.matsEqual(prod1, prod2)):
        return True
    else:
        return False