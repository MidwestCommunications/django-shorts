import re

from bitly_api import bitly_api

from django.contrib.sites.models import Site

from shorts.models import ShortURL


def findURL(text):
    #Run the text through a regex to find all urls.
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

    #Loop through list of found urls and shorten_url on each.
    if urls:
        for url in urls:
            return shorten_url(Site.objects.get_current(), url).shortened_url

    return 

def shorten_url(site, url):
    #Connect to bit.ly api and call bit.ly shorten method on passed in url.
    bitly = bitly_api.Connection('midwestcommunications', 'R_8cf0d869efb892d4f8bbfe3601fa84c2')

    #make sure url isn't already stored locally, shorten it, and save to database.
    if not ShortURL.objects.filter(original_url=url):
        bitly_url = bitly.shorten(url)
        shortened_url = ShortURL(site=site, original_url=url, shortened_url=bitly_url['url'])
        shortened_url.save()
    else:
        shortened_url = ShortURL.objects.get(original_url=url)

        return shortened_url

    return shortened_url