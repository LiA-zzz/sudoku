import tkinter as tk
from board import board

class sudokuGUI:
    def __init__(self):
        self.sudoku = board()
        self.root = tk.Tk()
        self.root.title("Sudoku")
        self.boardFrame = tk.Frame(master=self.root,borderwidth=1)
        self.buttonFrame = tk.Frame(master = self.root, borderwidth = 1)
        self.createGrid(self.boardFrame,self.sudoku.board)
        self.createButtons(self.buttonFrame)
        self.boardFrame.pack()
        self.buttonFrame.pack()
        self.root.mainloop() 
    
    def on_close_solution(self):
        if "solutionWindow" in self.__dict__:
            self.solutionWindow.destroy()
            del self.solutionWindow

    def showSolution(self):
        if "solutionWindow" not in self.__dict__:
            self.solutionWindow = tk.Toplevel(self.root)
            self.solutionWindow.title("Solution")
            self.solutionWindow.protocol("WM_DELETE_WINDOW",self.on_close_solution)
            self.createGrid(self.solutionWindow,self.sudoku.getSolution())
        
    def confirmAction(self):
        pass

    def createGrid(self,inFrame,withGrid):
        for i in range(9):
            for j in range(9):
                frame = tk.Frame(master = inFrame, borderwidth = 5)
                frame.grid(row=i,column=j,padx=3,pady=0)
                if withGrid[i][j] != '0':
                    label = tk.Label(master=frame,text=str(withGrid[i][j]))
                    label.pack()
                else:
                    entry = tk.Entry(master=frame,width=2,)
                    entry.pack()

    def createButtons(self,inFrame):
        solveButton = tk.Button(master=inFrame,text='Show Solution',command = self.showSolution)
        solveButton.grid(row=0,column=0)
        resetButton = tk.Button(master=inFrame,text='Reset',command = self.confirmAction())
        resetButton.grid(row=0,column=1)
    
    def updateWindow(self):
        for i in range(9):
            for j in range(9):
                frame = tk.Frame(master = self.boardFrame, borderwidth = 5)
                frame.grid(row=i,column=j,padx=3,pady=0)
                if self.sudoku.board[i][j] != '0':
                    label = tk.Label(master=frame,text=str(self.sudoku.board[i][j]))
                    label.pack()
                else:
                    entry = tk.Entry(master=frame,width=2,)
                    entry.pack()

sudokuGUI()