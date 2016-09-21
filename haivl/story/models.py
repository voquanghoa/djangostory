from __future__ import unicode_literals

from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=1024)
    video_url = models.CharField(max_length=30)
    image = models.ImageField()

