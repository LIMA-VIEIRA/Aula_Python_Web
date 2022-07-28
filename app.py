from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask("hello")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Post(db.Model):

    _tablename_='posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(70), nullable=False)
    body = db.Column(db.String(500)) 
    created = db.Column(db.DateTime, nullable=False, defaut=datetime.now)
    user_id = db.Column(db.Integer, db.Foreignkei('user.id'))

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        username = db.Column(db.String(20), nullable=True, unique=True, index=True)
        email = db.Column(db.String(64), nullable=False, unique=True)
        password_hash = db.Column(db.String(128), nullable=False)
        posts = db. relationship('Post', backref= 'author') 

db.create_all()

@app.route("/")
def index():
    posts = Post.query.all()
    # BUSCA NO BANCO OS POSTS
    return render_template("index.html", posts=posts)

@app.route("/populate")
def populate():
    user = Paulo(username= 'Paulo', email="g@g.com", password_hash='a')
    Post1 = post(title="Post 1", body= "Texto do Post", author="user")
    Post2 = post(title="Post 2", body= "Texto do Post", author="user") 
    db.session(user)
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()
    return redirect(url_for('index'))