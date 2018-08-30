from app import app
import urllib.request
import json
from .models import movie

Movie = movie.Movie

# getting the api key from .config file
api_key = app.config['MOVIE_API_KEY']

# getting the url from .config
base_url = app.config['MOVIE_API_BASE_URL']


def process_results(movie_list):
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:

            movie_object = Movie(id, title, overview, poster,
                                 vote_average, vote_count)
            movie_results.append(movie_object)

    return movie_results


def get_movies(category):

    get_movies_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        movies_data = url.read()
        json_movies_response = json.loads(movies_data)

        movie_results = None

        if json_movies_response['results']:
            movies_lib = json_movies_response['results']
            movie_results = process_results(movies_lib)

    return movie_results


def get_movie(id):
    get_movie_details_url = base_url.format(id, api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id, title, overview,
                                 poster, vote_average, vote_count)

    return movie_object


def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(
        api_key, movie_name)

    with urllib.request.urlopen(search_movie_url) as url:
        movies = url.read()
        json_movies = json.loads(movies)
        movies_results = None
        if json_movies['results']:
            movies_lib = json_movies['results']
            movies_results = process_results(movies_lib)
    return movies_results
