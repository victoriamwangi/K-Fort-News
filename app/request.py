from app import app
import urllib.request, json
from .models import source

Source = source.Source

api_key  = app.config['API_KEY']
base_url = app.config['API_BASE_URL']


def get_news(sources):
    get_news_url = base_url.format(sources, api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        # print(get_news_url)
        get_news_response = json.loads(get_news_data)
        # print(get_news_response)
        
        
        news_results = None
        
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
            
    return news_results

def process_results(news_list):
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        url= news_item.get('url')
        
        if name:
            news_object = Source(id, name, url)
            news_results.append(news_object)
    print( news_list)       
    return news_results
            
            

