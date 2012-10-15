from django.db import models
from django.contrib.sites.models import Site


class ShortURL(models.Model):
    site = models.ForeignKey(Site)
    original_url = models.URLField(blank=True)
    shortened_url = models.URLField(blank=True)


    class Meta:
        verbose_name = "Shortened URL"

    def __unicode__(self):
        return self.original_url + ' --- [' + self.shortened_url + ']'