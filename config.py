import os

class Config:

    MOVIE_API_BASE_URL ='https://newsapi.org/v2/everything?{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('NEWS_API_KEY')
    



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}