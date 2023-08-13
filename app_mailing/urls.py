from django.urls import path

from app_mailing import views

app_name = 'app_mailing'

urlpatterns = [
    path('', views.index, name='index')
]