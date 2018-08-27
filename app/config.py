class Config:
    '''
    general parent class for configurations
    '''
    pass


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
