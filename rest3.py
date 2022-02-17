from flask import Flask,request,jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os


#Inisialisasi library
app = Flask(__name__)
api = Api(app)
CORS(app)

#konfigurasi database
db = SQLAlchemy(app)
basedir = os.path.dirname(os.path.abspath(__file__))
database = "sqlite:///" + os.path.join(basedir, "db.sqlite")
app.config["SQLAlchemy_DATABASE_URI"] = database

db.create_all()

#database model
class ModelDatabase(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nama = db.Column(db.String(100))
    nim = db.Column(db.Integer)
    #method menyimpan
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

db.create_all()
#variabel global
identitas = {}

class KResource(Resource):
    def get(self):
        query = ModelDatabase.query.all()
        
        output = [{
            "nama":data.nama,
            "nim":data.nim  
        } for data in query
        ]
        
        response = {
            "data":output 
        }
        return response
        
    
    def post(self):
        dataNama = request.form["nama"]
        dataNim = request.form["nim"]
        
        #masukkan data ke model
        model = ModelDatabase(nama=dataNama,nim=dataNim)
        model.save()
        
        response = {"msg":"berhasil ditambah"}
        return response, 200

api.add_resource(KResource,"/api",methods=["GET","POST"])

if __name__ == '__main__':
    app.run(debug=True,port=5002)
    