import cvxpy as cp
import numpy as np
import gurobipy
import cvxopt

# class problem():
#
#     def getVars(self):

def solve(grid):
    x1 = cp.Variable((9, 9), integer=True)
    x2 = cp.Variable((9, 9), integer=True)
    x3 = cp.Variable((9, 9), integer=True)
    x4 = cp.Variable((9, 9), integer=True)
    x5 = cp.Variable((9, 9), integer=True)
    x6 = cp.Variable((9, 9), integer=True)
    x7 = cp.Variable((9, 9), integer=True)
    x8 = cp.Variable((9, 9), integer=True)
    x9 = cp.Variable((9, 9), integer=True)

    var_mapping = {'1': x1, '2': x2, '3': x3, '4': x4, '5': x5, '6': x6, '7': x7, '8': x8, '9': x9}
    vars = [x1, x2, x3, x4, x5, x6, x7, x8, x9]

            # return [x1, x2, x3, x4, x5, x6, x7, x8, x9], var_mapping

        # def makeConstraints(self, grid):

    #
    constraints = []

    for var in vars:
        consts = [var <= 1, var >= 0, cp.sum(var) == 9, cp.sum(var, axis=1) == [1] * 9,
                  cp.sum(var, axis=0) == [1] * 9]
        for i in range(0, 3):
            for j in range(0, 3):
                consts.append(cp.sum(var[i * 3:(i + 1) * 3, j * 3:(j + 1) * 3]) == 1)
        constraints += consts

    for i in range(0, 9):
        for j in range(0, 9):
            cell = i * 9 + j
            val = grid[cell]
            if val != '':
                constraints.append(var_mapping[val][i,j] == 1)
            constraints.append(x1[i, j] + x2[i, j] + x3[i, j] + x4[i, j] + x5[i, j] + x6[i, j] + x7[i, j] + x8[i, j] + x9[i, j] == 1)

    problem = cp.Problem(cp.Minimize(cp.sum(x1)), constraints)
    problem.solve(solver = 'GUROBI')

    soln = np.zeros(shape=(9, 9))
    ct = 1
    for v in vars:
        for i in range(0, 9):
            for j in range(0, 9):
                if v.value[i, j] == 1:
                    soln[i, j] = ct
        ct += 1


    return soln

    # def __init__(self, grid):
    #     self.vars = getVars(self)
    #     self.constraints = makeConstraints(self, grid)


