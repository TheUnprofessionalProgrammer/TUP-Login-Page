from datetime import datetime
from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import os

local_server = True
app = Flask(__name__)
app.secret_key = "super-secret-key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/loginsignup"
db = SQLAlchemy(app)

class Login(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    date = db.Column(db.String(20), nullable=True)

class Sign(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    date = db.Column(db.String(20), nullable=True)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        date = datetime.now()
        log = Login(username=username, email=email, password=password, date=date)
        db.session.add(log)
        db.session.commit()

    return render_template('login.html')

@app.route('/sign', methods = ['GET', 'POST'])
def signup():
    if (request.method == 'POST'):
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        password = request.form.get('password')
        date = datetime.now()
        sign = Sign(name=name, phone=phone, email=email, password=password, date=date)
        db.session.add(sign)
        db.session.commit()

    return render_template('sign.html')


app.run()