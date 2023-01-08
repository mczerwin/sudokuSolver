# sudokuSolver
This repo serves as a generalized Linear Program to solve any feasible Sudoku problem. 

Running locally, run the interface.py file to bring up a 9x9 grid. Input the given sudoku values and press "Solve!"

If running on a server, run server_solver.py to deploy a Flask API that takes in requests with a body of the form:
{"problem": "8nnnnnnnnnn36nnnnnn7nn9n2nnn5nnn7nnnnnnn457nnnnn1nnn3nnn1nnnn68nn85nnn1nn9nnnn4nn"}

where n's represent blank cells, and values are associated left to right, top to bottom.




must pip install cvxopt to us glpk solver