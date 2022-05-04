from flask import render_template
from ..request import get_sources, get_articles
from . import main 



@main.route('/')
def index():
    
    source = get_sources()
    title = "Kfort"
   
    return render_template('index.html', title = title, news_sources = source)

@main.route('/article/<id>')
def articles(id):
    source_articles = get_articles(id)

        
    return render_template('article.html', source_articles = source_articles)



@main.route('/about')
def about():
    title = "about"
    return render_template('about.html' ,title =title)

