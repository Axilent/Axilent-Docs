"""
Models for Axilent Docs.
"""
from django.db import models

class Category(models.Model):
    """
    A content category.
    """
    name = models.CharField(unique=True, max_length=100)
    
    def __unicode__(self):
        return self.name

class Article(models.Model):
    """
    A documentation article.
    """
    path = models.CharField(max_length=200,unique=True)
    title = models.CharField(max_length=100)
    contents = models.TextField(blank=True)
    content_key = models.CharField(null=True, max_length=100)
    category = models.ForeignKey(Category,related_name='articles')
    
    def __unicode__(self):
        return self.title



    