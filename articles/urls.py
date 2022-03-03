from django.urls import path
from . import views



urlpatterns = [
    path(route='' , view=views.ArticlesView.as_view() , name='articles_page')
]