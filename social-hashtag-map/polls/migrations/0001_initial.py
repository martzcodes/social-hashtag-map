# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hashtag', models.CharField(max_length=200)),
                ('tweet_count', models.IntegerField(default=0)),
                ('insta_count', models.IntegerField(default=0)),
                ('verified_count', models.IntegerField(default=0)),
                ('unverified_count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Insta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
                ('content_id', models.CharField(unique=True, max_length=200)),
                ('known_user', models.BooleanField(default=False)),
                ('caption_text', models.CharField(max_length=200, null=True, blank=True)),
                ('content_type', models.CharField(max_length=200, null=True, blank=True)),
                ('thumbnail_link', models.CharField(max_length=200, null=True, blank=True)),
                ('image_link', models.CharField(max_length=200, null=True, blank=True)),
                ('lat', models.DecimalField(null=True, max_digits=20, decimal_places=17, blank=True)),
                ('lon', models.DecimalField(null=True, max_digits=20, decimal_places=17, blank=True)),
                ('link', models.CharField(max_length=200, null=True, blank=True)),
                ('content_date', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialSetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_type', models.CharField(default=b'TW', max_length=2, choices=[(b'TW', b'Twitter'), (b'IN', b'Instagram')])),
                ('api_name', models.CharField(max_length=200)),
                ('api_client_id', models.CharField(max_length=200, null=True, blank=True)),
                ('api_client_secret', models.CharField(max_length=200)),
                ('api_access_token', models.CharField(max_length=200, null=True, blank=True)),
                ('api_last_id', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=200)),
                ('van_name', models.CharField(max_length=200, null=True, blank=True)),
                ('tweet_count', models.IntegerField(default=0)),
                ('insta_count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
                ('known_user', models.BooleanField(default=False)),
                ('content', models.CharField(max_length=200, null=True, blank=True)),
                ('content_id', models.CharField(unique=True, max_length=200)),
                ('content_type', models.CharField(max_length=200, null=True, blank=True)),
                ('lat', models.DecimalField(null=True, max_digits=20, decimal_places=17, blank=True)),
                ('lon', models.DecimalField(null=True, max_digits=20, decimal_places=17, blank=True)),
                ('link', models.CharField(max_length=200, null=True, blank=True)),
                ('profile_pic', models.CharField(max_length=200, null=True, blank=True)),
                ('content_date', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Verified',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(unique=True, max_length=200)),
                ('twitter_name', models.CharField(max_length=200, null=True, blank=True)),
                ('twitter_id', models.CharField(max_length=200, null=True, blank=True)),
                ('instagram_name', models.CharField(max_length=200, null=True, blank=True)),
                ('instagram_id', models.CharField(max_length=200, null=True, blank=True)),
                ('runkeeper_name', models.CharField(max_length=200, null=True, blank=True)),
                ('runkeeper_id', models.CharField(max_length=200, null=True, blank=True)),
                ('tweet_count', models.IntegerField(default=0)),
                ('insta_count', models.IntegerField(default=0)),
                ('instas', models.ManyToManyField(to='polls.Insta')),
                ('tweets', models.ManyToManyField(to='polls.Tweet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(to='polls.Verified'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hashtag',
            name='instas',
            field=models.ManyToManyField(to='polls.Insta'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hashtag',
            name='tweets',
            field=models.ManyToManyField(to='polls.Tweet'),
            preserve_default=True,
        ),
    ]
