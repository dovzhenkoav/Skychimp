from django.urls import path
from django.views.decorators.cache import cache_page

from app_blog import views


app_name = 'app_blog'


urlpatterns = [
    path('', cache_page(60)(views.BlogListView.as_view()), name='blog_list'),
    path('post/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
]
