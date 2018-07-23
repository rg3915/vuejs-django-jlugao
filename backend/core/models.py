from django.db import models


class Links(models.Model):
    url = models.TextField()
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
