# mini-project
mini project on NQuenes
# Problem 0n NQuenes
import sys
import tkinter

def printSolution(board):
    root=tkinter.Tk()
    for i in range(N): 
        for j in range(N):
            if(board[i][j]==1):
                #board[i][j]="#";
                tkinter.Label(root,text=" # ",fg="RED",bg="GREEN").grid(row=i,column=j)
            else:
                #print (board[i][j], end = " ")
                tkinter.Label(root,text=" @ ",fg="GREEN",bg="ORANGE").grid(row=i,column=j)
            #label.pack()
       # print()
    root.mainloop()

# A utility function to check if a queen can 
# be placed on board[row][col]. Note that this 
# function is called when "col" queens are 
# already placed in columns from 0 to col -1. 
# So we need to check only left side for 
# attacking queens 
def isSafe(board, row, col): 

    # Check this row on left side 
    for i in range(col): 
        if board[row][i] == 1: 
            return False

    # Check upper diagonal on left side 
    for i, j in zip(range(row, -1, -1), 
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False

    # Check lower diagonal on left side 
    for i, j in zip(range(row, N, 1), 
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False

    return True

def solveNQUtil(board, col): 
    
    # base case: If all queens are placed 
    # then return true 
    if col >= N: 
        return True

    # Consider this column and try placing 
    # this queen in all rows one by one 
    for i in range(N): 

        if isSafe(board, i, col): 
            
            # Place this queen in board[i][col] 
            board[i][col] = 1

            # recur to place rest of the queens 
            if solveNQUtil(board, col + 1) == True: 
                return True;

            # If placing queen in board[i][col] 
            # doesn't lead to a solution, then 
            # queen from board[i][col] 
            board[i][col] = 0

    # if the queen can not be placed in any row in 
    # this colum col then return false 
    return False;

# This function solves the N Queen problem using Backtracking.
def solveNQ():
    board = [[0 for j in range(N)]for i in range(N)]

    if solveNQUtil(board, 0) == False: 
        print ("Solution does not exist")
        return False;

    printSolution(board) 
    return True
    
N=int(input("enter the size of matrix : "))
if(N>0):
    if(N<15):
        solveNQ()
    elif(N>=15):
        print("That entered ", N ,"makes the execution time High")
        print("Enter '0' to wait untill execute \nEnter '1' to exit the program \nEnter '2' to enter the new value to NQuenes ")
        n=int(input())
        if(n==0):
            solveNQ()
        elif(n==1):
            sys.exit()
        elif(n==2):
            Nn=int(input("Enter new Matrix value :"))
            N=Nn
            solveNQ()
else:
    root1=tkinter.Tk()
    #window=tkinter.title(root1,text="error")
    label=tkinter.Label(root1,text="Invalid Number\n Try another Number",fg="RED",bg="BLACK")
    label.pack()
    tkinter.mainloop()
    #print("Negative numbers are not allowed to enter for the formation of NQuenes");


