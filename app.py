from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/bye')
def bye():
    retJson = {
                'field1': "field 1 data",
                'field2': "field 2 data"
            }
    return jsonify(retJson)

@app.route('/add', methods=["POST"])
def add():
    reqDict = request.get_json()
    x = reqDict["x"]
    y = reqDict["y"]
    z = x+y
    retJson = {
                'z': z
            }
    return jsonify(retJson), 200

if __name__ == "__main__":
    app.run(debug=true)
