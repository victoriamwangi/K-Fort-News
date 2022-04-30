from flask import render_template
from app import app
from .request import get_news


@app.route('/')
def index():
    
    sources = get_news('bbc-news')
    title = "BBC"
    
    return render_template('index.html', title = title, news_sources = sources)

# @app.route('')