import urllib.request, json
from .models import Source, Article

# Source = source.Source
api_key = None
base_url = None
article_url = None

def configure_request(app):
    global api_key, base_url, article_url
    api_key = app.config['API_KEY']
    base_url = app.config['API_BASE_URL']
    article_url = app.config['ARTICLE_BASE_URL']





def get_sources():
    get_sources_url = base_url.format( api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
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
   
    return  sources_results
            
            

def get_articles(id):
    get_articles_details_url = article_url.format(id, api_key)
  
    
    with urllib.request.urlopen(get_articles_details_url) as url:#open url
       articles_details_data = url.read() #read url
       articles_details_response = json.loads(articles_details_data) #convert into py dictionaries
   
      
        
       articles_results =None
       if articles_details_response["articles"]:
            articles_list = articles_details_response.get('articles')
            articles_results = process_articles(articles_list)
       return articles_results
    

def process_articles( articles_list):
    articles_results = []
    for articles_item in  articles_list:
        id =  articles_item.get('id')
        author=  articles_item.get('author')
        title = articles_item.get('title')
        description =  articles_item.get('description')
        url =  articles_item.get('url')
        urlToImage=  articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
       
        
        if title:
             articles_object = Article(id,author, title, description, url,  urlToImage, publishedAt)
             articles_results.append( articles_object)
   
    return  articles_results
