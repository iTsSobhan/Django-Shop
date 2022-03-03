from django.contrib import admin
from .models import (ArticleCategory , Article)





class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'url_title' , 'parent' , 'is_active']
    list_editable = ['url_title' , 'parent' , 'is_active']
    
    

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title' , 'slug' , 'is_active']
    list_editable = ['is_active']
    



admin.site.register(ArticleCategory , ArticleCategoryAdmin)
admin.site.register(Article , ArticleAdmin)