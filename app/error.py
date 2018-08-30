from app import app
from flask import render_template


@app.errorhandler(404)
def four0four(error):
    return render_template('error.html'),404
