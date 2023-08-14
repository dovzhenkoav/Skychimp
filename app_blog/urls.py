from django.urls import path

from app_blog import views


app_name = 'app_blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
]