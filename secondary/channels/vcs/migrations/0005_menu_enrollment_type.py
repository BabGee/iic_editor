# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-14 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20170708_1642'),
        ('vcs', '0004_auto_20171008_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='enrollment_type',
            field=models.ManyToManyField(blank=True, to='crm.EnrollmentType'),
        ),
    ]
