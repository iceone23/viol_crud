from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt_secret_key'

#database config
app.config['MONGO_URI'] = 'mongodb://localhost:27017/violdb'

mongo = PyMongo(app)
jwt = JWTManager(app)
violations = mongo.db.violations
users = mongo.db.users
# enable CORS
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    current_user = users.find_one({'login' : data['login']})

    if not current_user:
        return {'message' : 'User ' + data['login'] + ' does not exist'}
    
'''    if users.check_password_hash(data['password']:
        access_token = create_access_token(identity = data['username'])
        refresh_token = create_refresh_token(identity = data['username'])
        return {
            'message' : 'User has successfuly login',
            'access_token' : access_token,
            'refresh_token' : refresh_token
        }
'''
@app.route('/users', methods=['GET'])
#@jwt_required 
def getAll_users():
    output = []
    for q in users.find():
        output.append({"public_id": q["public_id"], "name": q["name"], "login": q["login"],
                      "password": q["password"], "admin": q["admin"]})
    return jsonify({'users': output})

@app.route('/user/<public_id>', methods=['GET'])
#@jwt_required 
def get_user(public_id):
    user = users.find_one({'public_id' : public_id})
    if not user:
        return jsonify({'message': 'No user found!'})
    user_data = {"public_id" : user["public_id"], "name" : user["name"], "login" : user["login"],
                 "password" : user["password"], "admin" : user["admin"]}
    return jsonify({'user' : user_data})

@app.route('/user/<public_id>', methods=['DELETE'])
#@jwt_required 
def delete_user(public_id):
    user = users.delete_one({'public_id' : public_id})
    if not user:
        return jsonify({'message': 'No user found!'})

    return jsonify({'message' : 'User has been deleted'})

@app.route('/user/<public_id>', methods=['PUT'])
#@jwt_required 
def edit_user(public_id):
    data = request.get_json()

    hashed_pass = generate_password_hash(data['password'], method='sha256')
    if users.find_one({'public_id' : public_id}):
        users.update_one({'public_id' : public_id}, {'$set': {'name': data['name'],
        'login': data['login'], 'password' : hashed_pass, 'admin' : data['admin']}})
        return jsonify({'message': 'User was updated'})
    else:
        return jsonify({'message' : 'No users found!'})

@app.route('/user', methods=['POST'])
#@jwt_required 
def create_user():
    data = request.get_json()

    hashed_pass = generate_password_hash(data['password'], method='sha256')
    if users.find_one({'login' : data['login']}):
        return jsonify({'message' : 'User ' + data['login'] + ' already exist'})
    else:
        users.insert_one({"public_id": str(uuid.uuid4()), "name": data['name'], "password": hashed_pass,
                      "login": data['login'], "admin": False})
        return jsonify({'message' : 'New user created'})

@app.route('/violations', methods=['GET'])
#@jwt_required 
def all_violations():

    output = []
    for q in violations.find():
        output.append({"public_id": q["public_id"], "date": q["date"], "whoFound": q["whoFound"], "network": q["network"],
                       "ipAdress" : q["ipAdress"], "department" : q["department"], "militaryUnit" : q["militaryUnit"],
                       "deslocation" : q["deslocation"], "subordinate" : q["subordinate"], "normDoc" : q["normDoc"],
                       "violCont" : q["violCont"], "volumeInf" : q["volumeInf"], "sourceDoc" : q["sourceDoc"],
                       "incomeDoc" : q["incomeDoc"]})
    return jsonify({ 'data': output})

@app.route('/violation_delete/<data_index>', methods=['DELETE'])
#@jwt_required 
def delete_violation(data_index):
    if violations.find_one({"public_id": data_index}):
        violations.delete_one({"public_id" : data_index})
        return jsonify({'message' : 'Violation has been deleted'})
    else:
        return jsonify({'message': 'No violation found!'})

@app.route('/violation_edit/<data_index>', methods=['PUT'])
#@jwt_required 
def edit_violation(data_index):
    data = request.get_json()
    data["date"] = datetime.strftime(datetime.strptime(request.json['date'],"%Y-%m-%d"), "%d.%m.%Y")
    if violations.find_one({"public_id" : data_index}):
        violations.update_one({"public_id" : data_index}, {'$set': {"date": data["date"],
            "whoFound": data["whoFound"], "network": data["network"],
            "ipAdress" : data["ipAdress"], "department" : data["department"],
            "militaryUnit" : data["militaryUnit"], "deslocation" : data["deslocation"],
            "subordinate" : data["subordinate"], "normDoc" : data["normDoc"],
            "violCont" : data["violCont"], "volumeInf" : data["volumeInf"],
            "sourceDoc" : data["sourceDoc"], "incomeDoc" : data["incomeDoc"]}})
        return jsonify({'message': 'Violation was updated'})
    else:
        return jsonify({'message' : 'No violations found!'})

@app.route('/violation_new', methods=['POST'])
#@jwt_required 
def add_violation():
    #convert time to dd.mm.yyyy format
    date = datetime.strftime(datetime.strptime(request.json['date'],"%Y-%m-%d"), "%d.%m.%Y")
    whoFound = request.json['whoFound']
    network = request.json['network']
    ipAdress = request.json['ipAdress']
    department = request.json['department']
    militaryUnit = request.json['militaryUnit']
    deslocation = request.json['deslocation']
    subordinate = request.json['subordinate']
    normDoc = request.json['normDoc']
    violCont = request.json['violCont']
    volumeInf = request.json['volumeInf']
    sourceDoc = request.json['sourceDoc']
    incomeDoc = request.json['incomeDoc']
    #sourceFile = request.files['sourceFile']
    #incomeFile = request.files['incomeFile']

    id = str(uuid.uuid4())

    
    violations.insert_one({"public_id": id, "date": date, "whoFound": whoFound, "network": network,
                "ipAdress" : ipAdress, "department" : department, "militaryUnit" : militaryUnit,
                "deslocation" : deslocation, "subordinate" : subordinate, "normDoc" : normDoc,
                "violCont" : violCont, "volumeInf" : volumeInf, "sourceDoc" : sourceDoc,
                "incomeDoc" : incomeDoc})
    return jsonify({'message' : 'violation was added'})

"""@app.route('/upload', methods=['POST'])
def upload(fileName):
    with grid_fs.new_file(filename=fileName) as fp:
        fp.write(request.data)
        file_id=fp._id

    if grid_fs.find_one(file_id) is not None:
        return jsonify({'message' : 'file succesful uploaded'})
    else:
        return jsonify({'message' : 'file not uploaded'})
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0')