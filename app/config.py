class Config:
    API_BASE_URL = "https://newsapi.org/v2/top-headlines/sources?country=us&apiKey={}"
    ARTICLE_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    
    # API_KEY = '270eb01000ec4deeae78422bae9aca3d'
    

class DevConfig(Config):
    DEBUG = True
    
class ProdConfi(Config):
    pass