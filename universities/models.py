from __future__ import unicode_literals

from django.db import models
from departments.models import Department

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=255)
    direcction = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=50)

class HaveDepartment(models.Model):
    dep = models.ForeignKey(Department)
    uni = models.ForeignKey(University)

    class Meta:
        verbose_name = 'University-Deparment'
        verbose_name_plural = 'Universities-Departments'

    def __str__(self):
        return '%s %s' % (self.dep.name, self.uni.name)