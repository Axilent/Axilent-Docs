"""
Axilent content mappings.
"""
from axilent.hooks import ContentMapping
from docs.models import Article, Category

class ArticleMapping(ContentMapping):
    """
    Mapping for article.
    """
    model = Article
    content_type = 'Article'
    pk_field = 'path'
    save_to_axilent = False # Read only.
    
    def on_load(self,data,model):
        """
        Called when the local content is sync'd to the Axilent content item.  Must return
        the local model.
        """
        if 'path' in data:
            model.path = data['path']
        
        if 'title' in data:
            model.title = data['title']
        
        model.contents = data.get('contents',None)
        
        if 'category' in data:
            category, category_created = Category.objects.get_or_create(name=data['category'])
            model.category = category
        
        
        model.save()
        return model
    
    def on_save(self,data,model):
        """
        Called when the local content is saved.  Must return the data for Axilent.
        """
        data['path'] = model.path
        data['title'] = model.title
        data['category'] = model.category.name
        data['contents'] = model.contents
        return data

