class Source:
    def __init__(self,id, name, description, category, url, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.country = country
        self.category = category
        
        
class Article:
    def __init__(self,id,  author, title, description ,url, urlToImage, publishedAt):
        self.id = id
        self.author = author
        self.urlToImage = urlToImage
        self.title = title
        self.description = description
        self.url = url 
        self.publishedAt = publishedAt
        
        