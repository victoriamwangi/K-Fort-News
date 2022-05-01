class Config:
    API_BASE_URL = "https://newsapi.org/v2/top-headlines/sources?&apiKey={}"
    # 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    # 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=270eb01000ec4deeae78422bae9aca3d'
    
    # API_KEY = '270eb01000ec4deeae78422bae9aca3d'
    

class DevConfig(Config):
    DEBUG = True
    
class ProdConfi(Config):
    pass