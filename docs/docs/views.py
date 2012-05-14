"""
Views for Axilent-Docs.
"""
from django.shortcuts import render_to_response
from axilent.hooks import ContentChannel
from docs.models import Article

main_channel = ContentChannel('welcome')
dev_channel = ContentChannel('development')
getting_started_channel = ContentChannel('getting-started')

def index(request):
    """
    Home page.
    """
    articles = main_channel.get_models()
    #dev_articles = dev_channel.get_models()
    #gs_articles = getting_started_channel.get_models()
    dev_articles = None; gs_articles = None
    return render_to_response('index.html',{'message':'Hello biznatches.','articles':articles,'dev_articles':dev_articles,'gs_articles':gs_articles})

def article(request,path):
    """
    Gets the specified article.
    """
    print 'looking for article with path',path
    path = path[:-1] if path.endswith('/') else path
    article = Article.objects.get(path='/%s' % path)
    return render_to_response('article.html',{'article':article})

