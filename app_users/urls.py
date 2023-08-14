from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

#from app_users.views import RegisterView, verify_view, forget_email_view, recover_password_confirmation_view

app_name = 'app_users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='app_users/login.html'), name='login'),
    # path('verify/<int:code>', verify_view, name='verify'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('forget_email/', forget_email_view, name='forget_email'),
    # path('recover_conf/', recover_password_confirmation_view, name='recover_password')

]
