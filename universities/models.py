from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from departments.models import Department
from presidents.models import President
from statuses.models import Status

# Create your models here.

class University(models.Model):
    name = models.CharField(blank=False, max_length=255)
    direction = models.CharField(blank=False, max_length=255)
    fkdepartment = models.ForeignKey(Department)
    postal_code = models.CharField(blank=False, max_length=50)
    phone = models.CharField(blank=False, max_length=60)
    fax = models.IntegerField(blank=False)
    email = models.EmailField(blank=False, max_length=255)
    fkuser = models.ForeignKey(User)
    fkpresident = models.ForeignKey(President)
    observation = models.TextField(blank=False)
    history = models.TextField(blank=False)
    legal_constitution = models.TextField(blank=False)
    fkstatus = models.ForeignKey(Status)


# class HaveDepartment(models.Model):
#     dep = models.ForeignKey(Department)
#     uni = models.ForeignKey(University)

#     class Meta:
#         verbose_name = 'University-Deparment'
#         verbose_name_plural = 'Universities-Departments'

#     def __str__(self):
#         return '%s %s' % (self.dep.name, self.uni.name)