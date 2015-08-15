# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='instas',
            field=models.ManyToManyField(to='polls.Insta'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='tweets',
            field=models.ManyToManyField(to='polls.Tweet'),
            preserve_default=True,
        ),
    ]
