from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponse
from .models import Article




class ArticlesView(View):
    def get(self , request : HttpResponse):
        articles : Article = Article.objects.filter(is_active=True)
        return render(request=request , template_name='articles/articles.html' , context={'articles':articles})
    
    
    
def header_component(request : HttpResponse):
    return render(request=request , template_name='articles/header-component.html' , context={})



def footer_component(request : HttpResponse):
    return render(request=request , template_name='articles/footer-component.html' , context={})