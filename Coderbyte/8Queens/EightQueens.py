def EightQueens(strArr):
    chessBoard = [[0 for x in range(8)] for y in range(8)]
    for item in strArr:
        for 
        chessBoard[item[0]-1][item[1]-1] += 1
        # run check
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in chessBoard]))
    

inputData = [(2,2)]
EightQueens(inputData)