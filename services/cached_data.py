from django.conf import settings
from django.core.cache import cache

from app_blog.models import BlogPost
from app_mailing.models import Mailing, Client


def get_cached_post_datail(context):
    """Get cached post data if exists."""
    if settings.CACHE_ENABLED:
        key = f'post_datail{context.object.pk}'
        post = cache.get(key)
        if post is None:
            post = BlogPost.objects.get(pk=context.object.pk)
            cache.set(key, post, 60)
    else:
        post = BlogPost.objects.get(pk=context.object.pk)
    return post


def get_cached_index_data():
    """Get cached stasis"""
    if settings.CACHE_ENABLED:
        key_all_mailing_counter = f'index_data_all_mailing_counter'
        key_active_mailing_counter = f'index_data_active_mailing_counter'
        key_unique_client_counter = f'index_unique_client_counter'
        key_random_blogposts = f'index_random_blogposts'

        all_mailing_counter = cache.get(key_all_mailing_counter)
        active_mailing_counter = cache.get(key_active_mailing_counter)
        unique_client_counter = cache.get(key_unique_client_counter)
        random_blogposts = cache.get(key_random_blogposts)

        if all_mailing_counter is None or active_mailing_counter is None or unique_client_counter is None:
            all_mailing_counter = len(Mailing.objects.all())
            active_mailing_counter = len(Mailing.objects.filter(status='launched'))
            unique_client_counter = len(Client.objects.all().distinct('email'))
            random_blogposts = BlogPost.objects.order_by("?")[:3]

            cache.set(key_all_mailing_counter, all_mailing_counter, 60)
            cache.set(key_active_mailing_counter, active_mailing_counter, 60)
            cache.set(key_unique_client_counter, unique_client_counter, 60)
            cache.set(key_random_blogposts, random_blogposts, 60)
    else:
        all_mailing_counter = len(Mailing.objects.all())
        active_mailing_counter = len(Mailing.objects.filter(status='launched'))
        unique_client_counter = len(Client.objects.all().distinct('email'))
        random_blogposts = BlogPost.objects.order_by("?")[:3]
    return all_mailing_counter, active_mailing_counter, unique_client_counter, random_blogposts
