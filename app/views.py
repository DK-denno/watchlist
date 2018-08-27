from flask import render_template
# from app folder import the new instace of Flask stored under app 'variable'
from app import app
# Views


@app.route('/')
def index():
    '''
    a function that returns the whole of the page index.html
    '''
    message = 'hello DK'
    return render_template('index.html', greetings=message)


@app.route('/movie/<movie_id>')
def movie(movie_id):
    return render_template('movie.html', id=movie_id)
