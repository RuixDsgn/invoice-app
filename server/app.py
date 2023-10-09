from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://invoice_app_uq9z_user:1oNwvZHSYLxkgkAKB1w0HDcd7J1oMkfv@dpg-cki57veafg7c73evcfcg-a.oregon-postgres.render.com/invoice_app_uq9z'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from models import Instructor, School, Record, Invoice

if __name__ == '__main__':
    app.run(debug=True)
