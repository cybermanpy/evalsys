from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
# Create your models here.

class userProfiles(models.Model):
    pkuser = models.ForeingKey(User)
    pkprofile = models.ForeingKey(Profile)

    class Meta:
        verbose_name = 'User-Profile'
        verbose_name_plural = 'User-Profiles'

    def __str__(self):
        return '%s %s' % (self.pkuser.name, self.pkprofile.name)