import os

class Config:
    API_BASE_URL = "https://newsapi.org/v2/top-headlines/sources?country=us&apiKey={}"
    ARTICLE_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    API_KEY = os.environ.get('API_KEY')
    
    

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass
    
config_options ={
    'development': DevConfig,
    'production': ProdConfig
}