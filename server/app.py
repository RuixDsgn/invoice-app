from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, get_jwt, jwt_required
from flask_bcrypt import Bcrypt


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://invoice_app_uq9z_user:1oNwvZHSYLxkgkAKB1w0HDcd7J1oMkfv@dpg-cki57veafg7c73evcfcg-a.oregon-postgres.render.com/invoice_app_uq9z'
app.config["JWT_SECRET_KEY"] = 'dullescythe'
jwt = JWTManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
bcrypt = Bcrypt(app)

revoked_tokens = set()

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/register', methods=['POST'])
def register():
    from models import Instructor
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        name = request.json.get('name')
        email = request.json.get('email')

        hashed_password =  bcrypt.generate_password_hash(password).decode('utf-8')

        print(f"Received registration data: username={username}, password={password}, name={name}, email={email}")

        new_instructor = Instructor(username=username, password=hashed_password, name=name, email=email)
        db.session.add(new_instructor)
        db.session.commit()

        return jsonify({'message': 'Registration successful'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500

@app.route('/login', methods=['POST'])
def login():
    from models import Instructor
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    instructor = Instructor.query.filter_by(username=username).first()
    if instructor and bcrypt.check_password_hash(instructor.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({'msg': 'Bad username or password'}), 401
    

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

if __name__ == '__main__':
    app.run(debug=True)
