# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(null=True, verbose_name=b'Age'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='github_url',
            field=models.URLField(max_length=255, null=True, verbose_name=b'GitHub URL', blank=True),
        ),
    ]
