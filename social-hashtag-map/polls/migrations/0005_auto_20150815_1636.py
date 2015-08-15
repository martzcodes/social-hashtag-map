# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20150815_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='instas',
            field=models.ForeignKey(blank=True, to='polls.Insta', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='tweets',
            field=models.ForeignKey(blank=True, to='polls.Tweet', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ForeignKey(blank=True, to='polls.Verified', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verified',
            name='instas',
            field=models.ForeignKey(blank=True, to='polls.Insta', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verified',
            name='tweets',
            field=models.ForeignKey(blank=True, to='polls.Tweet', null=True),
            preserve_default=True,
        ),
    ]
