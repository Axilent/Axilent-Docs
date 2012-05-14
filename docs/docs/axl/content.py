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
    pk_field = 'Path'
    save_to_axilent = False # Read only.
    
    def on_load(self,data,model):
        """
        Called when the local content is sync'd to the Axilent content item.  Must return
        the local model.
        """
        if 'Path' in data:
            model.path = data['Path']
        
        if 'Title' in data:
            model.title = data['Title']
        
        model.contents = data.get('Content',None)
        
        if 'Category' in data:
            category, category_created = Category.objects.get_or_create(name=data['Category'])
            model.category = category
        
        
        model.save()
        return model
    
    def on_save(self,data,model):
        """
        Called when the local content is saved.  Must return the data for Axilent.
        """
        data['Path'] = model.path
        data['Title'] = model.title
        data['Category'] = model.category.name
        data['Contents'] = model.contents
        return data

