# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150815_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content_id',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
