from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Status(models.Model):
    description = models.CharField(max_length=60)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ('id',)