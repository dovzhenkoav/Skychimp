from django.views import generic

from app_blog.models import BlogPost
from services.cached_data import get_cached_post_datail


class BlogListView(generic.ListView):
    """View all posts."""
    model = BlogPost
    template_name = 'app_blog/blog_list.html'


class BlogDetailView(generic.DetailView):
    """Blog post page."""
    model = BlogPost
    template_name = 'app_blog/blog_detail.html'

    def get_object(self, queryset=None):
        """Increase view counter on viewing."""
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        """Get cached data if exists."""
        context_data = super().get_context_data(**kwargs)
        post = get_cached_post_datail(self)
        context_data['object'] = post
        return context_data
