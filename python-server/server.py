from flask import Flask, request
from flask_restful import Resource, Api
import calendar
import time

app = Flask(__name__)
api = Api(app)

todos = {}

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class digital(Resource):
    def get(self):
        print("recebi figital")
        idDig = request.args.get("id")
        num = request.args.get("num")
        return {idDig: num,"ts":calendar.timegm(time.gmtime())}

class analogico(Resource):
    def get(self):
        print("recebi analgoic")
        idAn = request.args.get("id")
        num = request.args.get("num")
        return {idAn: num,"ts":calendar.timegm(time.gmtime())}

#class TodoSimple(Resource):
#    def get(self, todo_id):
#        return {todo_id: todos[todo_id]}
#
#    def put(self, todo_id):
#        todos[todo_id] = request.form['data']
#        return {todo_id: todos[todo_id]}

#api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(HelloWorld, '/')
api.add_resource(digital, '/digital')
api.add_resource(analogico, '/analogico')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    #app.run(debug=True)
