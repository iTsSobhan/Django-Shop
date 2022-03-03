from django.urls import path
from . import views


urlpatterns = [
    path(route='' , view=views.ContactUsView.as_view() , name='contact_us_page') ,
    path(route='create-profile/' , view=views.CreateProfileView.as_view() , name='create_profile_page') ,
    path(route='profiles/' , view=views.ProfilesView.as_view() , name='profiles_page')
]