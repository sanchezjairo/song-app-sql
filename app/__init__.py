from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from app.config import Config
import os


app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

###########################
# Authentication
###########################

#  authentication setup code here!
bcrypt = Bcrypt(app)
login_manager = LoginManager()

login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


###########################
# Blueprints
###########################

from app.main.routes import main as main_routes
app.register_blueprint(main_routes)

from app.auth.routes import auth as auth_routes
app.register_blueprint(auth_routes)

with app.app_context():
    db.create_all()
