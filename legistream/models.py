from django.db import models


class Streams(models.Model):
    timestamp = models.IntegerField()
    streams_dict = models.CharField(max_length=300)
