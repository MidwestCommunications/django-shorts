import re

from bitly_api import bitly_api

from django.contrib.sites.models import Site

from shorts.models import ShortURL


def findURL(text):
    #Run the text through a regex to find all urls.
    urls = re.compile(r"""(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>\[\]]+|\(([^\s()<>\[\]]+|(\([^\s()<>\[\]]+\)))*\))+(?:\(([^\s()<>\[\]]+|(\([^\s()<>\[\]]+\)))*\)|[^\s`!(){};:'".,<>?\[\]]))""")
    matches = []

    def process_matches(m):
        matches.append(m.group(0))
        #Loop through list of found urls and shorten_url on each.
        if matches:
            for url in matches:
                return shorten_url(Site.objects.get_current(), url).shortened_url
        return

    new_text = urls.sub(process_matches, text)

    return new_text

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