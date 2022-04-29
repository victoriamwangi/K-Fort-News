class Config:
    API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    pass

class DevConfig(Config):
    DEBUG = True
    
class ProdConfi(Config):
    pass