from __future__ import unicode_literals

from django.db import models

# Create your models here.

class President(models.Model):
    full_name = models.CharField(max_length=60)
    position = models.CharField(max_length=60)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ('id',)