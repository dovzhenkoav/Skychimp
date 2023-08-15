from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def mediapath(image_url: str):
    """Get url to media folder."""
    return settings.MEDIA_URL + str(image_url)
