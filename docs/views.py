"""
Views for Axilent-Docs.
"""
from django.shortcuts import render_to_response
from axilent.hooks import ContentChannel
from docs.models import Article
from axilent.utils import client
from django.template.defaultfilters import slugify
from sharrock.client import HttpClient
from django.conf import settings

main_channel = ContentChannel('welcome')
dev_channel = ContentChannel('development')
getting_started_channel = ContentChannel('getting-started')
related_article_channel = ContentChannel('related-articles')
tutorials_channel = ContentChannel('tutorials')


def index(request):
    """
    Home page.
    """
    articles = main_channel.get()
    dev_articles = dev_channel.get()
    gs_articles = getting_started_channel.get()
    tutorials_articles = tutorials_channel.get()
    return render_to_response('index.html',{'message':'Hello biznatches.','articles':articles,'dev_articles':dev_articles,'gs_articles':gs_articles,'tutorials_articles':tutorials_articles})

def article(request,path):
    """
    Gets the specified article.
    """
    c = client('axilent.content')
    article = c.getcontentbyuniquefield(content_type='Article',field_name='path',field_value=path)
    related_articles = related_article_channel.get(basekey=article['key'])
    return render_to_response('article.html',{'article':article,'related_articles':related_articles})

def category(request,category_name):
    """
    Gets articles in the specified category.
    """
    category_channel = ContentChannel(slugify(category_name))
    articles = category_channel.get()
    return render_to_response('category.html',{'articles':articles,'category':category_name})

def article_index(request):
    """
    The actual main index of all the articles.
    """
    gs_articles = getting_started_channel.get()
    dev_articles = dev_channel.get()
    return render_to_response('article_index.html',{'gs_articles':gs_articles,'dev_articles':dev_articles})


# ==========
# = Search =
# ==========

search_client = HttpClient('https://www.axilent.net/api','axilent.content','beta3',auth_user=settings.AXILENT_API_KEY)

def search(request):
    """
    Search.
    """
    results = search_client.search(content_types='Article',query=request.GET['q'])
    return render_to_response('search_results.html',{'results':results})
