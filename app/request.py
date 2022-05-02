from app import app
import urllib.request, json
from .models.source import Source, Article

# Source = source.Source


api_key  = app.config['API_KEY']
base_url = app.config['API_BASE_URL']
article_url = app.config['ARTICLE_BASE_URL']


def get_sources():
    get_sources_url = base_url.format( api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        print(get_sources_url)
        get_sources_response = json.loads(get_sources_data)
       
        
        
        news_results = None
        
        if get_sources_response['sources']:
            news_results_list = get_sources_response['sources']
            news_results = process_results(news_results_list)
            
    return news_results

def process_results( sources_list):
    sources_results = []
    for sources_item in  sources_list:
        id =  sources_item.get('id')
        name=  sources_item.get('name')
        description =  sources_item.get('description')
        url=  sources_item.get('url')
        country =  sources_item.get('country')
        category =  sources_item.get('category')
        
        
        if id:
             sources_object = Source(id,name, description,category, url,  country)
             sources_results.append( sources_object)
    print( sources_results[1])   
    print("hehe")  
    return  sources_results
            
            
def get_articles(source):
    get_articles_url = article_url.format(source, api_key)
    
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        article_results = None
        
        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)
        
    return article_results


def process_articles(article_list):
    article_results = []
    for article_item in article_list:
        author = article_item.get("author")
        title= article_item.get("title")
        description= article_item.get("description")
        urlToImage = article_item.get("urlToImage")
        if urlToImage:
            article_object = Article(id, author, title, description, urlToImage) 
            article_results.append(article_object)
            
    return article_results
             
            
    
