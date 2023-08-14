from django.views import generic

from app_blog.models import BlogPost


class BlogListView(generic.ListView):
    model = BlogPost
    template_name = 'app_blog/blog_list.html'
