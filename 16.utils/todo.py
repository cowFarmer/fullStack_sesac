from flask import Flask, request
from flask_restx import Api, Resource


app = Flask(__name__)
api = Api(app)

todos = {}

@api.route('/<string:todo_id>')
class HelloWorld(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}
    
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

if __name__ == '__main__':
    app.run(port=8080, debug=True)