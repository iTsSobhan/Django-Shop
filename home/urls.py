from django.urls import path
from . import views


urlpatterns = [
    path(route='' , view=views.HomeView.as_view() , name='home_page') ,
    path(route='about-us' , view=views.AboutView.as_view() , name='about_us_page')
]