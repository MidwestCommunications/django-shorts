from bitly_api import bitly_api

from django.contrib.sites.models import Site

from shorts.models import ShortURL


def shorten_url(site, url):
    bitly = bitly_api.Connection('username', 'api_key')
    bitly_url = bitly.shorten(url)

    if not ShortURL.objects.filter(shortened_url=bitly_url['url']):
        shortened_url = ShortURL(site=site, original_url=url, shortened_url=bitly_url['url'])
        shortened_url.save()

    return

def expand_url(site, url):
    bitly = bitly_api.Connection('username', 'api_key')
    bitly_url = bitly.expand(shortUrl=url)

    original_url = bitly_url[0]['long_url']

    return original_url