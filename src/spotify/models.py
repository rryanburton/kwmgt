from django.db import models


class Artist(models.Model):
    external_urls = models.URLField(null=True)
    # followers_href = models.CharField(max_length=255, null=True)
    followers_total = models.IntegerField(null=True)
    # genres = models.CharField(max_length=255, null=True)
    # href = models.URLField(null=True)
    spotify_id = models.CharField(max_length=255, null=True)
    image = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    popularity = models.IntegerField(null=True)
    type = models.CharField(max_length=255, null=True)
    uri = models.CharField(max_length=255, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'spotify'
