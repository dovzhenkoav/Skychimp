from django.conf import settings
from django.core.cache import cache

from app_blog.models import BlogPost


def get_cached_post_datail(context):
    if settings.CACHE_ENABLED:
        key = f'post_datail{context.object.pk}'
        post = cache.get(key)
        if post is None:
            post = BlogPost.objects.get(pk=context.object.pk)
            cache.set(key, post, 60)
    else:
        post = BlogPost.objects.get(pk=context.object.pk)
    return post
