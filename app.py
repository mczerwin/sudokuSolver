from flask import Flask
from flask import request
import solver
import numpy as np
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/solve', methods=['POST'])
def solve():
    print(f'request: {request}')
    print(f'data: {request.data}')

    puzzle = request.json['puzzle']
    print(type(puzzle))
    print(puzzle)
    
    soln = solver.solve(formatBody(puzzle))
    print(soln)
    print(type(soln))
    solved = formatResponse(soln)
    return solved


def formatBody(req):
    arr = []
    for f in req:
        if f == 'n':
            arr.append('')
        else:
            arr.append(f)
    return arr

def formatResponse(solved):
    return str(np.reshape(solved, (1,81))).replace('.', '').strip("[]").replace(' ', '')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)