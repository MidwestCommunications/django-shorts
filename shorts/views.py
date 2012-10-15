from django.contrib.sites.models import get_current_site
from django.shortcuts import render, redirect

import shorts.utils


def index(request):

    return render(request, 'shorts/shorts_test.html', {})

def shorten(request):
    current_site = get_current_site(request)
    shortened_url = shorts.utils.shorten_url(current_site, request.POST['url'])

    return redirect('/shorts/', shortened_url=shortened_url)