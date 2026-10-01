
from flask_sqlalchemy import SQLAlchemy

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']='be43c68e374426231eaee27462438213'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes