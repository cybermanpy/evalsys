from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(blank=False, max_length=100)
    level = models.CharField(blank=False, max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)

class UserProfile(models.Model):
    fkuser = models.ForeignKey(User)
    fkprofile = models.ForeignKey(Profile)

    class Meta:
        verbose_name = 'User-Profile'
        verbose_name_plural = 'User-Profiles'

    def __str__(self):
        return '%s %s' % (self.fkuser.username, self.fkprofile.name)