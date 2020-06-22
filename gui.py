import tkinter as tk
from board import board

def createWindow():
    sudoku = board()
    
    root = tk.Tk()
    for i in range(9):
        for j in range(9):
            frame = tk.Frame(master = root, borderwidth = 1)
            frame.grid(row=i,column=j,padx=3,pady=0)
            if sudoku.board[i][j] != 0:
                label = tk.Label(master=frame,text=str(sudoku.board[i][j]))
                label.pack()
            else:
                entry = tk.Entry(master=frame,width=2)
                entry.pack()

    root.mainloop()

createWindow()