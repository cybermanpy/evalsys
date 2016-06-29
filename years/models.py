from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Year(models.Model):
    description = models.CharField(max_length=255)
    date = models.CharField(max_length=4)
    
    def __str__(self):
        return self.description
    
    class Meta:
        ordering = ('id',)
