from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Add(Resource):
    def post(self):
        postData = request.get_json()
        x = postData["x"]
        y = postData["y"]
        x = int(x)
        y = int(y)

        ret = x + y
        retMap = {
                    'Message': ret,
                    'Status Code': 200
                }
        return jsonify(retMap)

api.add_resource(Add, "/add")

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

if __name__ == "__main__":
    app.run(debug=true)
