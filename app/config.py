class Config:
    '''
    general parent class for configurations
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'


class prodConfig(Config):
    '''
    production child configuration class
    '''
    pass


class devConfig(Config):
    '''
    development child configuration class
    '''
    pass

    DEBUG = True
