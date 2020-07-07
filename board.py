import os, random
import solver

class board:
    def __init__(self):
        self.board = [] #store the orignal board for the reset button of the gui. (resets state back to original board)
        prefix = os.getcwd() + "\\boards\\"
        openFile = open(prefix+random.choice(os.listdir("boards")),'r')
        for line in openFile:
            row = [val for val in line.split() if val != '\n']
            self.board.append(row)
        openFile.close()
        
        self.solution = [row.copy() for row in self.board]
        self.solvingBoard = [row.copy() for row in self.board] #get the user input information and update the status of this board.
        solver.solve(self.solution)
        
    
    def __repr__(self):
        #temp console view of sudoku board.
        vert = "*===================================*\n"
        mid = "| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} |"
        split = "|===|===|===|===|===|===|===|===|===|\n"
        retStr = vert
        counter = 0
        for row in self.board:
            if counter%3 == 0 and counter != 0:
                retStr+=split
            retStr += mid.format(*row)+"\n"
            counter+=1
        retStr+=vert
        return retStr
    
    def getSolution(self):
        return self.solution

    def getBoard(self):
        return self.board
    
    def modifyBoard(self,val,row,col):
        pass

    def compareToAnswer(self,board):
        pass
            

