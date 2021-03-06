#Sudoku Solving / Checking Methods
def checkRow(board: list,row: int)-> bool:
    rowVals = {"1","2","3","4","5","6","7","8","9"}
    try:
        for val in board[row]:
            if val != "0":
                rowVals.remove(val)
    except KeyError:
        return False
    return True
    
def checkCol(board: list,col: int)->bool:
    colVals = {"1","2","3","4","5","6","7","8","9"}
    try:
        for row in range(9):
            if board[row][col] != '0':
                colVals.remove(board[row][col])
    except Exception:
        return False
    return True

def checkSubGrid(board: list,row: int,col: int)->bool:
    subVals = {"1","2","3","4","5","6","7","8","9"}
    rowStart = 0
    colStart = 0
    #Determine which subgrid the square is a part of
    if 3 <= row < 6:
        rowStart = 3
    elif 6 <= row < 9:
        rowStart = 6
        
    if 3 <= col < 6:
        colStart = 3
    elif 6 <= col < 9:
        colStart = 6
    try:
        for r in range(rowStart,rowStart+3):
            for c in range(colStart,colStart+3):
                if board[r][c] != '0':
                    subVals.remove(board[r][c])
    except Exception:
        return False
    return True

def recurse(board: list)->bool:
    r,c = -1,-1
    for row in range(0,9):
        for col in range(0,9):
            if board[row][col] == '0':
                r,c = row,col
                break
                
    if r == -1 and c == -1:
        return True
    
    for test in range(1,10):
        board[r][c] = str(test)
        if isValid(board,r,c) and recurse(board):
            return True
        board[r][c] = '0'
    return False

def isValid(board: list,row: int,col: int)-> bool:
    validRow = checkRow(board,row)
    validCol = checkCol(board,col)
    validSub = checkSubGrid(board,row,col)
    return validRow and validCol and validSub
    
def solve(board: list) -> None:
    recurse(board)
    

