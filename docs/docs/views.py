"""
Views for Axilent-Docs.
"""
from django.shortcuts import render_to_response

def index(request):
    """
    Home page.
    """
    return render_to_response('index.html',{'message':'Hello bitches.'})

