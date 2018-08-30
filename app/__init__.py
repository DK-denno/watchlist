from flask import Flask
# initialising the application
# new instance of the Flask class from flask module
app = Flask(__name__, instance_relative_config=True)
#from app import views
# importing the views.py file to make is cotent accessible to this file
from .config import devConfig
# importing the development child configuration class
# setting up configuration
app.config.from_object(devConfig)
app.config.from_pyfile('config.py')

from flask_bootstrap import Bootstrap
from app import views
from app import error
# initialising flask exentions

bootstrap = Bootstrap(app)
