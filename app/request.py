from app import app
import urllib.request, json
from .models.source import Source

# Source = source.Source


api_key  = app.config['API_KEY']
base_url = app.config['API_BASE_URL']


def get_news(source):
    get_news_url = base_url.format(source, api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        print(get_news_url)
        get_news_response = json.loads(get_news_data)
       
        
        
        news_results = None
        
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
            
    return news_results

def process_results(news_list):
    news_results = []
    for news_item in news_list:
        news_title = news_item.get('title')
        description = news_item.get('description')
        url= news_item.get('url')
        title = news_item.get('title')
        # print (article)
     
        
        if news_title:
            news_object = Source(news_title, description, url, title)
            news_results.append(news_object)
            
    return news_results
            
            

