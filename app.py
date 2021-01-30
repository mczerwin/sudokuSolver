from flask import Flask, request, jsonify
import server_solver
import json

app = Flask(__name__)


@app.route('/solve')
def solve():
    
    data = json.loads(request.data)
    soln = server_solver.solve(list(data['problem']))
    print(soln)
    
    return soln



if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)