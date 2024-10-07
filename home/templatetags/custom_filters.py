from django import template
from urllib.parse import urlparse

register = template.Library()


@register.filter
def extract_domain(url):
    parsed_uri = urlparse(url)
    domain = parsed_uri.netloc
    return domain
