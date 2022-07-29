from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, current
from werkzeug.security import check_password_hash, generate_passaword_hash

app = Flask("hello")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEI"] = "pudim"

db = SQLAlchemy(app)
login = LoginManager(app)

class Post(db.Model):

    _tablename_='posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(70), nullable=False)
    body = db.Column(db.String(500)) 
    created = db.Column(db.DateTime, nullable=False, defaut=datetime.now)
    user_id = db.Column(db.Integer, db.Foreignkei('users.id'))

    class User(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        username = db.Column(db.String(20), nullable=True, unique=True, index=True)
        email = db.Column(db.String(64), nullable=False, unique=True)
        password_hash = db.Column(db.String(128), nullable=False)
        posts = db. relationship('Post', backref= 'author') 
    
    def set_password( self, password):
        self.password_hash =generate_password_hash(password)

    def check_password(self, password):
            return check_password_hesh(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

db.create_all()

@app.route("/")
def index():
    posts = Post.query.all()
    # BUSCA NO BANCO OS POSTS
    return render_template("index.html", posts=posts)

@app.route('/register', methods=["GET","POST"])
def register():
     
    
    return render_template('register.html')


@app.route('/login')
def login():
    return register('login.html')