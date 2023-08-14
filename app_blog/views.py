from django.views import generic

from app_blog.models import BlogPost


class BlogListView(generic.ListView):
    model = BlogPost
    template_name = 'app_blog/blog_list.html'


class BlogDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'app_blog/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object
