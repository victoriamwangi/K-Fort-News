from flask import render_template
from app import app
from .request import get_sources, get_articles


@app.route('/')
def index():
    
    source = get_sources()
    title = "Kfort"
   
    return render_template('index.html', title = title, news_sources = source)

@app.route('/article')
def articles():
    source_articles = get_articles('bbc-news')
    
    return render_template('article.html', source_articles = source_articles)

# @app.route('article/<int: id')
# def article(id):
#     article = get_articles(id)
#     article_title = f'{article.title}'

#     return render_template('article.html', article_title = article_title)