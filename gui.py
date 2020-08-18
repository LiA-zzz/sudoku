<<<<<<< HEAD
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

    def resetBoard(self):
        for row in range(9):
            for col in range(9):
                widget = self.boardFrame.grid_slaves(row=row,column=col)
                try:
                    widget[0].children['!entry'].delete(0,'end')
                except Exception:
                    continue
        self.confirmFrame.destroy()

    def confirmReset(self):
        self.confirmFrame = tk.Toplevel(self.root)
        self.confirmFrame.title("Reset?")
        btnFrame = tk.Frame(self.confirmFrame)
        yes_action = tk.Button(btnFrame,text='Yep', command=self.resetBoard)
        no_action = tk.Button(btnFrame,text='Nope', command=self.confirmFrame.destroy)
        yes_action.grid(row=0,column=0,padx=10,pady=10)
        no_action.grid(row=0,column=1,padx=10,pady=10)
        action_prompt = tk.Label(self.confirmFrame,text="Are you sure you want to reset the board?")

        action_prompt.grid(row=0,column=0)
        btnFrame.grid(row=1,column=0)
    
    def correctAnswer(self):
        self.confirmFrame = tk.Toplevel(self.root)
        self.confirmFrame.title("Congratulations!")
        btnFrame = tk.Frame(self.confirmFrame)
        yes_action = tk.Button(btnFrame,text='Yep', command=self.resetBoard)
        no_action = tk.Button(btnFrame,text='Nope', command=self.confirmFrame.destroy)
        yes_action.grid(row=0,column=0,padx=10,pady=10)
        no_action.grid(row=0,column=1,padx=10,pady=10)
        action_prompt = tk.Label(self.confirmFrame,text="Congrats! You solved this sudoku board. Would you like to reset the board?")

        action_prompt.grid(row=0,column=0)
        btnFrame.grid(row=1,column=0)

    def incorrectAnswer(self):
        self.confirmFrame = tk.Toplevel(self.root)
        self.confirmFrame.title("Please try again")
        action_prompt = tk.Label(self.confirmFrame,text="Unfortunately this is not a valid solution for this sudoku board.\n\nBoxes Highlighted in green are correct while boxes highlighted in red are not.")
        action_prompt.grid(row=0,column=0)

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
        solveButton.grid(row=0,column=1)
        resetButton = tk.Button(master=inFrame,text='Reset',command = self.confirmReset)
        resetButton.grid(row=0,column=2)
        checkAnswer = tk.Button(master=inFrame,text='Check Answer',command = self.checkAnswers)
        checkAnswer.grid(row=0,column=0)
    
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
    
    def checkAnswers(self):
        for row in range(9):
            for col in range(9):
                widget = self.boardFrame.grid_slaves(row=row,column=col)
                try:
                    self.sudoku.solvingBoard[row][col] = widget[0].children['!entry'].get()
                    if (self.sudoku.solvingBoard[row][col] != self.sudoku.solution[row][col]):
                        widget[0].config(bg="red")
                    else:
                        widget[0].config(bg="green")
                except Exception:
                    continue
        if (self.sudoku.solvingBoard == self.sudoku.solution):
            self.correctAnswer()
        else:
            self.incorrectAnswer()

=======
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

    def resetBoard(self):
        for row in range(9):
            for col in range(9):
                widget = self.boardFrame.grid_slaves(row=row,column=col)
                try:
                    widget[0].children['!entry'].delete(0,'end')
                except Exception:
                    continue
        self.confirmFrame.destroy()

    def confirmReset(self):
        self.confirmFrame = tk.Toplevel(self.root)
        self.confirmFrame.title("Reset?")
        btnFrame = tk.Frame(self.confirmFrame)
        yes_action = tk.Button(btnFrame,text='Yep', command=self.resetBoard)
        no_action = tk.Button(btnFrame,text='Nope', command=self.confirmFrame.destroy)
        yes_action.grid(row=0,column=0,padx=10,pady=10)
        no_action.grid(row=0,column=1,padx=10,pady=10)
        action_prompt = tk.Label(self.confirmFrame,text="Are you sure you want to reset the board?")

        action_prompt.grid(row=0,column=0)
        btnFrame.grid(row=1,column=0)
    
    def correctAnswer(self):
        self.confirmFrame = tk.Toplevel(self.root)
        self.confirmFrame.title("Congratulations!")
        btnFrame = tk.Frame(self.confirmFrame)
        yes_action = tk.Button(btnFrame,text='Yep', command=self.resetBoard)
        no_action = tk.Button(btnFrame,text='Nope', command=self.confirmFrame.destroy)
        yes_action.grid(row=0,column=0,padx=10,pady=10)
        no_action.grid(row=0,column=1,padx=10,pady=10)
        action_prompt = tk.Label(self.confirmFrame,text="Congrats! You solved this sudoku board. Would you like to reset the board?")

        action_prompt.grid(row=0,column=0)
        btnFrame.grid(row=1,column=0)

    def incorrectAnswer(self):
        self.confirmFrame = tk.Toplevel(self.root)
        self.confirmFrame.title("Please try again")
        action_prompt = tk.Label(self.confirmFrame,text="Unfortunately this is not a valid solution for this sudoku board.")
        action_prompt.grid(row=0,column=0)

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
        solveButton.grid(row=0,column=1)
        resetButton = tk.Button(master=inFrame,text='Reset',command = self.confirmReset)
        resetButton.grid(row=0,column=2)
        checkAnswer = tk.Button(master=inFrame,text='Check Answer',command = self.checkAnswers)
        checkAnswer.grid(row=0,column=0)
    
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
    
    def checkAnswers(self):
        for row in range(9):
            for col in range(9):
                widget = self.boardFrame.grid_slaves(row=row,column=col)
                try:
                    self.sudoku.solvingBoard[row][col] = widget[0].children['!entry'].get()
                except Exception:
                    continue
        if (self.sudoku.solvingBoard == self.sudoku.solution):
            self.correctAnswer()
        else:
            self.incorrectAnswer()

>>>>>>> c95b4e6ebd2e34c3bc7235caf1d45b24593017c8
sudokuGUI()