from app import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Instructor(db.Model):
    __tablename__ = 'instructors'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

class School(db.Model):
    __tablename__ = 'schools'
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(80), nullable=False)

class Record(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    prep_time = db.Column(db.Float, nullable=False)
    class_time = db.Column(db.Float, nullable=False)
    post_class_time = db.Column(db.Float, nullable=False)
    commute_over_30mins = db.Column(db.Boolean, default=False)

    instructor_id = db.Column(db.Integer, db.ForeignKey('instructors.id'), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'), nullable=False)

    instructor = db.relationship('Instructor', backref='records')
    school = db.relationship('School', backref='records')

class Invoice(db.Model):
    __tablename__ = 'invoices'
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(20), unique=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)

    instructor_id = db.Column(db.Integer, db.ForeignKey('instructors.id'), nullable=False)

    instructor = db.relationship('Instructor', backref='invoices')


# after making changes to models.py:
# flask db init to initialize the migrations
# flask db migrate -m 'your message' to create the migration
# flask db upgrade to apply the migration and update the table