from flask import Flask,request,jsonify
from flask_restful import Resource, Api
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)

identitas = {}

class KResource(Resource):
    def get(self):
        return identitas
    
    def post(self):
        dataNama = request.form["nama"]
        dataNim = request.form["nim"]
        identitas["nama"] = dataNama
        identitas["nim"] = dataNim
        response = {"msg":"berhasil"}
        return response, 200

api.add_resource(KResource,"/api",methods=["GET","POST"])

if __name__ == '__main__':
    app.run(debug=True,port=5002)
    