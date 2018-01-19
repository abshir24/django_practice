from __future__ import unicode_literals

from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    