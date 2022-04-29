from app import app
import urllib.request, json
from .models import source

Source = source.Source

api_key  = app.config['API_ KEY']
base_url = app.config['API_BASE_URL']


def get_news(sources):
    get_news_url = base_url.format(sources, api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        print(get_news_url)
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response['results']:
            news_results_list = get_news['results']
            news_results = process_results(news_results_list)
            
return news_results
            

