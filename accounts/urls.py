from django.urls import path
from . import views



urlpatterns = [
    path(route='login' , view=views.LoginView.as_view() , name='login_page') ,
    path(route='logout' , view=views.LogoutView.as_view() , name='logout_page') ,
    path(route='register' , view=views.RegisterView.as_view() , name='register_page') ,
    path(route='forget-password' , view=views.ForgetPasswordView.as_view() , name='forget_password_page') ,
    path(route='reset-password/<active_code>' , view=views.ResetPasswordView.as_view() , name='reset_password_page') ,
    path(route='activate-account/<str:email_active_code>' , view=views.ActivateAccountView.as_view() , name='activate_account_page')
]