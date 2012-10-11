import json

from django.db import models
from django.contrib.sites.models import Site


class ShortURL(models.Model):
    site = models.ForeignKey(Site)
    shortened_url = models.TextField(default='[{"original_url": "", "shortened_url": ""}]')

    

    class Meta:
        verbose_name = "short url"

    def __unicode__(self):
        return self.shortened_url