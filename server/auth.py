from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from app import app

app.config["JWT_SECRET_KEY"] = 'dullescythe'
jwt = JWTManager(app)

revoked_tokens = set()

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    name = request.json.get('name')
    email = request.json.get('email')

    hashed_password =  hashed_password(password)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username != username or password != password:
        return jsonify({'msg': 'Bad username or password'}), 401
    
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
   current_token = get_jwt()
   jti = current_token['jti']

   revoked_tokens.add(jti)

   return jsonify(message='Successfully logged out'), 200

# @app.route('/reset-password', methods=['POST'])
# @jwt_required()
# def reset_password():
#     new_password = request.json.get('new_password')
    
#     current_user = get_jwt_identity()
    
#     current_token = get_jwt()
#     jti = current_token['jti']
#     revoked_tokens.add(jti)
    
#     return jsonify(message="Password reset successful"), 200