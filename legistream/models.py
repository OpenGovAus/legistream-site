from django.db import models


class Streams(models.Model):
    streams_dict = models.CharField(max_length=300)
