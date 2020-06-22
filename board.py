import os, random

class board:
    def __init__(self):
        self.board = []
        #self.presetSquares = []
        prefix = os.getcwd() + "\\boards\\"
        openFile = open(prefix+random.choice(os.listdir("boards")),'r')
        for line in openFile:
            row = [int(val) for val in line.split() if val != '\n']
            self.board.append(row)
    
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
    
    

            

