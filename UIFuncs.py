# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 14:42:12 2021

@author: Obutler

- Non-mathematical functions for handling user input and output as well
as general-purpose functions.
"""

class matrix:
    mat = []
    rows = 0
    cols = 0
    label = ""
    
    def __init__(self, Mat, Rows, Cols):
        self.mat = Mat
        self.rows = Rows
        self.cols = Cols
    
    def simplify(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                if(abs(round(self.mat[i][j]) - self.mat[i][j]) < 1e-15):
                    self.mat[i][j] = round(self.mat[i][j])
        return

import os
import sys
import matFuncs as matf
import sqMatFuncs as sqmatf

def mainInterface(matrices, userIn):
    while(userIn != "exit"):
        if(userIn == "cancel"):
            del matrices[-1]
        
        clear()
        print("------------------")
        print("Your matrices:")
        printMatricesNicely(matrices)
        print("------------------")
        
        print("What would you like to do?\n\
0. Exit calculator\n\
1.1. Load matrices from file\n\
1.2. Input a matrix\n\
1.3. Add a label to a matrix\n\
1.4. Delete a matrix\n\
1.5. Delete all matrices\n\
1.6. Transpose a matrix\n\
1.7. Add two matrices\n\
1.8. Multiply two matrices\n\
1.9. Check if two matrices are equal\n\
1.10. Add rows of a matrix\n\
1.11. Swap two rows of a matrix\n\
1.12. Multiply row of matrix by scalar\n\
\nBelow functions can only be performed on square matrices\n\n\
2.1. Find the determinant of a matrix\n\
2.2. Find the trace of a matrix\n\
2.3. Invert a matrix\n\
2.4. Find the adjugate of a matrix\n\
2.5. Check whether two matrices commute")
        
        match input("Enter a choice: "):
            case "1.1": loadMats(matrices)
            case "1.2": userIn = inputMatrix(matrices)
            case "1.3": label(matrices)
            case "1.4": delMatrix(matrices)
            case "1.5": matrices.clear()
            case "1.6": matf.initTranspose(matrices)
            case "1.7": matf.initAddMatrices(matrices)
            case "1.8": matf.initMultiplyMatrices(matrices)
            case "1.9": matf.initMatsEqual(matrices)
            case "1.10": matf.initAddRows(matrices)
            case "1.11": matf.initSwapRows(matrices)
            case "1.12": matf.initMultiplyRow(matrices)
            case "2.1": sqmatf.initDet(matrices)
            case "2.2": sqmatf.trace(matrices)
            case "2.3": sqmatf.invertMatrix(matrices)
            case "2.4": sqmatf.initAdjugate(matrices)
            case "2.5": sqmatf.initMatsCommute(matrices)
            case "0": userIn = "exit"
            case _: print("\nInvalid function choice\n")

    return

# Determines whether input is a valid matrix.
# Returns (in order): (bool) validity, numRows, numCols
def isMatrix(mat):
    if(len(mat) == 1):
        return True, 1, 1
    
    for i in range(len(mat) - 1):
        if len(mat[i]) != len(mat[i + 1]):
            return False, 0, 0
        else:
            continue
    return True, len(mat), len(mat[0])

# Prints a single matrix nicely in row/column format.
def printMatrix(mat):
    for i in range(mat.rows):
        for j in range(mat.cols):
            print(f"{mat.mat[i][j]} ", end = "")
        print("")
    return

# Prints a list of matrices nicely formatted.
# Includes labels.
def printMatricesNicely(matrices):
    for i in range(len(matrices)):
        if(matrices[i].label != ""):
            print(f"{i + 1}. ({matrices[i].label}):")
        else:
            print(f"{i + 1}:")
        printMatrix(matrices[i])
        if(i != len(matrices) - 1):
            print("")
    return

# Clears console screen, helps mitigate clutter
# when running.
def clear():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")
    return

# Used in many functions for a user to select a
# valid matrix.
def chooseMatrix(matrices, message) -> int:
    while(True):
        choice = input(message)
        if(choice.isnumeric()):
            choice = int(choice) - 1
            if(choice < -1 or choice > len(matrices) - 1):
                print("Invalid matrix choice")
            else:
                return choice
        else:
            print("Invalid matrix choice")

def chooseRow(mat, message):
    while(True):
        choice = input(message)
        if(choice.isnumeric()):
            choice = int(choice) - 1
            if(choice < -1 or choice > mat.rows - 1):
                print("Invalid row choice")
            else:
                return choice
        else:
            print("Invalid row choice")

# Allows user to input their own matrices.
# Checks validity of input matrix with isMatrix()
def inputMatrix(matrices) -> str:
    tempMatrix = []
    # Loop as long as input is certainly not a valid matrix
    valid = False
    while(not valid):
        print("Begin entering rows of matrix. Separate row entries with spaces.")
        print("When you are finished entering rows, type \"done\"")
        print("If you would like to cancel inputting a matrix, type \"cancel\"")
        print("If you would like to exit the calculator, type \"exit\"")
        tempMatrix = []
        gettingInput = True
        rowIndex = 1
        while(gettingInput):
            row = []
            userIn = input(f"Row {rowIndex}: ")
            if(userIn == "done"):
                gettingInput = False
                continue

            elif(userIn == "cancel"):
                tempMatrix = [[0]]
                break
            
            elif(userIn == "exit"):
                # Need a valid matrix to break out of this loop.
                # Will break out of the next loop because userin == "exit"
                tempMatrix = [[0]]
                break
            
            else:
                entries = userIn.split()
                for i in range(len(entries)):
                    entry = entries[i]
                    if(entry.isnumeric()):
                        entry = float(entry)
                        if(entry.is_integer()):
                            entry = int(entry)
                        row.append(entry)
                    else:
                        print("Invalid character encountered in row.")
                        input("Press enter to continue")
                        return ""
                tempMatrix.append(row)
                rowIndex += 1
        
        valid, temprows, tempcols = isMatrix(tempMatrix)
        if(not valid):
            print("Invalid input matrix")
        else:
            newMatrix = matrix(tempMatrix, temprows, tempcols)
            matrices.append(newMatrix)
            return userIn

# Allows user to add a label to their matrix; purely
# aesthetic. Labels are used when diplaying matrices
# to the console.
def label(matrices):
    matrixChoice = chooseMatrix(matrices, "Which matrix would you like to label? Enter 0 to exit this function: ")
    if(matrixChoice == -1):
        return
    else:
        matrixLabel = input("Input desired matrix label: ")
        matrices[matrixChoice].label = matrixLabel
        return

# Removes a matrix from the matrices list.
# Also handles choosing which matrix to delete.
# *** Currently breaks order-based labelling *** #
def delMatrix(matrices):
    matrixChoice = chooseMatrix(matrices, "Which matrix would you like to delete? Enter 0 to exit this function: ")
    if(matrixChoice == -1):
        return
    else:
        del matrices[matrixChoice]
        return

# Allows user to save their matrices to a text file in a
# standard format. These text files can be read back in
# by another instance of the calculator with loadMats()
# without needing to specially format the file. If a user
# wants to manually create their own text file to be read
# in, they should familiarize themselves with the
# standard matrix output format of the calculator and
# write the file in that format.
def saveMats(matrices):
    outFile = input("What file would you like to output to (defaults to matsout.txt): ")
    if(outFile == ""):
        outFile = "matsout.txt"
    elif(".txt" not in outFile):
        outFile += ".txt"
    
    file = open(outFile, "w")
    
    # Change stdout of program to so that print() writes to output file
    original_stdout = sys.stdout
    sys.stdout = file
    
    printMatricesNicely(matrices)
    
    # Change stdout back to console
    sys.stdout = original_stdout
    file.close()
    return

# Reads in a text file of matrices written in the standard
# format, and loads those matrices into memory for use by
# the calculator.
def loadMats(matrices):
    # List text files in current directory for easy reference.
    filesList = os.listdir(".")
    print("\nText files in current directory:")
    for f in filesList:
        if f.endswith(".txt"):
            print(f)
    
    matrixFile = input("Input the name of the file to load: ")
    
    # Read contents of file into array for manipulation
    file = open(matrixFile, "r")
    matData = file.read()
    file.close()
    
    # Split matData into array of lines in file
    matData = matData.split("\n")
    tempRows = 0
    tempCols = 0
    tempMatrix = []
    tempLabel = ""
    
    # Loop through array of lines from file
    for row in matData:
        # If line has a colon in it, it is the beginning of a new matrix
        # It is possible that there is a label on this line as well
        if(":" in row):
            # If there is a period in this line, we know there is a label
            if("." in row):
                # Split and trim the line to obtain the matrix label
                tempLabel = row.split(".")[-1]
                tempLabel = tempLabel[2:-2]
        # If a row is empty, the current matrix is finished being read.
        elif(row == ""):
            # Check that the lines we have been reading are a valid matrix.
            valid, tempRows, tempCols = isMatrix(tempMatrix)
            if(valid):
                # If valid, append new matrix to matrices list
                tempMatrix = matrix(tempMatrix, tempRows, tempCols)
                tempMatrix.label = tempLabel
                matrices.append(tempMatrix)
            else:
                # Stop parsing on encountering an invalid matrix
                print(f"File contains invalid matrix at line {row.index}:\n{row}")
                return
            # Reset tempMatrix and tempLabel for reading next matrix
            tempMatrix = []
            tempLabel = ""
        else:
            # Append matrix entries in current line as a new row in tempMatrix
            tempRow = []
            for val in row.strip().split(" "):
                val = float(val)
                if val.is_integer():
                    val = int(val)
                tempRow.append(val)
            tempMatrix.append(tempRow)
    return