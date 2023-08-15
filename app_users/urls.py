from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from app_users import views


app_name = 'app_users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='app_users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('register/confirmation/', views.UserRegisterConfirmationView.as_view(), name='register_confirmation'),
    path('verify/<int:code>', views.verify_view, name='verify'),
    path('recover_password/', views.recover_password_view, name='recover_password'),
    path('recover_password_confirmation/', views.RecoverPasswordConfirmationView.as_view(), name='recover_password_confirmation')

]
