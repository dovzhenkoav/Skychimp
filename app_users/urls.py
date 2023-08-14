from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

#from app_users.views import RegisterView, verify_view, forget_email_view, recover_password_confirmation_view

app_name = 'app_users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='app_users/login.html'), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),


]
