# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 02:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('presidents', '0001_initial'),
        ('universities', '0003_university_fkdepartment'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='email',
            field=models.EmailField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='fax',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='fkpresident',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='presidents.President'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='fkstatus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='statuses.Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='fkuser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='history',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='legal_contitution',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='observation',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='phone',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
