from flask import Flask,request ,jsonify
from flask_restful import reqparse, abort, Api, Resource
import ServerTools
import os
import sys

def setup():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path.split("\\")[:-1]
    dir_path.append("EditPdf")
    sys.path.append("\\".join(dir_path))

setup()
import Edittools

app = Flask(__name__)
api = Api(app)


class QuestionStructur(Resource):
    def get(self):
        return ServerTools.question_folder_structur()

class OrderPrint(Resource):
    def post(self):
        data = request.get_json(force=True)
        try:
            security = ServerTools.username_password()
            if(data['username'] != security['username'] or data['password'] != security['password']):
                resp = {"message": "username or password is wrong"}
                return resp

            EditObj = Edittools.Edit()
            EditObj.render(ServerTools.question_folder_path()+data['question_address']
            , EditObj.find_target_address(), data)
            resp = {"message": "everything is ok"}
            return resp
        except:
            resp = {"message": "error"}
            return resp


api.add_resource(QuestionStructur, '/structure')
api.add_resource(OrderPrint, '/print')

if __name__ == '__main__':
    app.run(debug=True)


"""
{
        "username": "admin",
        "password": "helloworld",
        "question_address": "\\set1\\2.pdf",
        "question_code" : "76512",
        "major": "riazi",
        "question_type": "hard",
        "recive_time": "20:20:20",
        "price":"2",
        "team_code":"1008",
        "team_name":"amazing men",
        "score":"10",
        "last_info" : {"1003":"20", "1004":"20", "500":"10"}
}
"""