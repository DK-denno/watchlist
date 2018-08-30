from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from .forms import ReviewForm
# from app folder import the new instace of Flask stored under app 'variable'
from app import app
# Views
from .request import get_movies
# importing the get_movies() function
from .models import review

from .request import get_movie
from .request import search_movie
Review = review.Review


@app.route('/')
def index():
    '''
    a function that returns the whole of the page index.html
    '''
    message = 'hello DK'
    title = 'Home-Welcome mofos'
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    search_movie = request.args.get('movie_query')
    print(search_movie)
    if search_movie:
        return redirect(url_for('search', movie_name=search_movie))
    else:

        return render_template('index.html',
                               title=title,
                               popular=popular_movies,
                               upcoming=upcoming_movies,
                               greetings=message
                               )


@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id)
    return render_template('movie.html', title=title, revies=reviews, movie=movie)


@app.route('/dennis')
def dennis():
    return render_template('dennis.html')


@app.route('/search/<movie_name>')
def search(movie_name):
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html', movies=searched_movies, title=title)


@app.route('/movie/review/new/<int:id>', methods=['GET', 'POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id, title, movie.poster, review)
        new_review.save_review()
        return redirect(url_for('movie', id=movie.id))

    title = f'{movie.title} review'
    return render_template('new_review.html', title=title, review_form=form, movie=movie)


if __name__ == '__main__':
    app.run()
