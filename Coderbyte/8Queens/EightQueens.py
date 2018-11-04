## TO-DO: make check for diagonals

'''
Using the Python language, have the function EightQueens(strArr) 
read strArr which will be an array consisting of the locations 
of eight Queens on a standard 8x8 chess board with no other pieces 
on the board. The structure of strArr will be the following: 
["(x,y)", "(x,y)", ...] where (x,y) represents the position of 
the current queen on the chessboard (x and y will both range 
from 1 to 8 where 1,1 is the bottom-left of the chessboard and 
8,8 is the top-right). Your program should determine if all of 
the queens are placed in such a way where none of them are attacking 
each other. If this is true for the given input, return the string 
true otherwise return the first queen in the list that is attacking 
another piece in the same format it was provided. 

For example: if strArr is 
["(2,1)", "(4,2)", "(6,3)", "(8,4)", "(3,5)", "(1,6)", "(7,7)", "(5,8)"] 
then your program should return the string true. 
The corresponding chessboard of queens for this input is below 
(taken from Wikipedia). 

'''

def EightQueens(strArr):
    # create matrix 8x8 with zeros
    chessBoard = [[0 for x in range(8)] for y in range(8)]
    for item in strArr:
        # fill ones for current element
        k = item[0]
        m = item[1]
        # if the spot is already taken, spit out error
        if chessBoard[k][m]==1:
            print("error: (",k,",",m,")")
            return
        # fill ones horizontally
        for i in range(8):
            chessBoard[k][i]=1
        # fill ones vertically
        for j in range(8):
            chessBoard[j][m]=1
        for i in range(8):
            if k+i < 8 and m+i < 8:
                chessBoard[k+i][m+i]=1
            elif k+i >= 8 and m+i < 8:
                chessBoard[k+i-8][m+i]=1
            elif k+i >= 8 and m+i >= 8:
                chessBoard[k+i-8][m+i-8]=1
            elif k+i < 8 and m+i >= 8:
                chessBoard[k+i][m+i-8]=1




            
    
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in chessBoard]))
    

inputData = [(2,2)]
EightQueens(inputData)