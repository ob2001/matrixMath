# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:48:38 2021

@author: Obutler

- MatrixMath is a program that performs matrix operations on user-defined matrices.
- The user can input arbitrary matrices and perform any (WIP) matrix operation
they wish.
- The program keeps a running memory both of matrices the user has input, and matrices
that have been output from previous operations.
- Support for unary and binary matrix operations.
- Optionally save matrices to a text file when exiting program.
- Optionally load matrices from a file.
"""

### ---------------------------------- ###
### Entry point for matrixMath program ###
### ---------------------------------- ###

import UIFuncs as ui

# Initialize lists
# Matrices stores all of the matrices, rows stores the mnumber
# of rows in each matrix, cols stores the number of columns in
# each matrix, labels stores the labels assigned to each matrix (if any)
matrices = []
userIn = ""

# Run main calculator. Returns when user decides to exit from within
# this function.
ui.mainInterface(matrices, userIn)

# Remove 0 matrix generated when exiting from within the inputMatrix function
if(len(matrices) >= 2 and matrices[-1].mat == [[0]]):
    del matrices[-1]

# Ask to save matrices only if there are valid matrices in memory
if(len(matrices) >= 2 or (matrices != [] and matrices[0].mat != [[0]])):
    ui.clear()
    print("------------------")
    print("Your matrices:")
    ui.printMatricesNicely(matrices)
    print("------------------")
    
    save = input("Would you like to save your matrices to a text file? (y/n): ")
    if(save == "y"):
        ui.saveMats(matrices)
        
print("Thanks for using the matrix calculator!")