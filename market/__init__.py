from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login_page'
login_manager.login_message_category='info'
login_manager.login_message='برای استفاده از این قسمت ابتدا باید وارد حساب کاربری خودتان شوید'
app.config['SECRET_KEY']='114ed81981d557cd49294d9d'
from market import routes
