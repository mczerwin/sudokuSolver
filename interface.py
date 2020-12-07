from tkinter import*
import solver
import numpy as np

master=Tk()
master.title("Sudoku Solver")

entrys = [Entry(master) for i in range(81)]

for i in range(0,9):
    for j in range(0,9):
        entrys[i*9+j] .grid(row=i, column=j)

def show_soln(soln):
    soln_list = np.reshape(soln, (1,81))
    for i in range(len(entrys)):
        entrys[i].insert(0, soln_list[0,i])

def submit():
    nums = [entry.get() for entry in entrys]
    soln = solver.solve(nums)
    show_soln(soln)
    print(soln)




button1=Button(master, text="Solve!", command = submit)
button1.grid(row=9, column=4)

master.mainloop()