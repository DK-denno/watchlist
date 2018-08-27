from flask import Flask
# initialising the application
# new instance of the Flask class from flask module
app = Flask(__name__)
from app import views
# importing the views.py file to make is cotent accessible to this file
