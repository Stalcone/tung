# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('first_letter', models.CharField(blank=True, max_length=2)),
                ('image_url', models.URLField(blank=True)),
                ('review_text', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('grade', models.IntegerField()),
                ('year', models.IntegerField(default=3000)),
                ('genre', models.CharField(blank=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('first_letter', models.CharField(blank=True, max_length=2)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='persons')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TVShow',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.URLField(blank=True)),
                ('genre', models.CharField(blank=True, max_length=255)),
                ('creator', models.ManyToManyField(related_name='created', to='movies.Person')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='tvshows')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TVShowSeason',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('number', models.IntegerField()),
                ('image_url', models.URLField(blank=True)),
                ('year', models.IntegerField()),
                ('review_text', models.TextField()),
                ('grade', models.IntegerField()),
                ('actors', models.ManyToManyField(related_name='tvshow_starred', to='movies.Person')),
                ('tvshow', models.ForeignKey(to='movies.TVShow', related_name='seasons')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='tvshow_seasons')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='starring', to='movies.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(blank=True, related_name='directed_by', to='movies.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='movies'),
            preserve_default=True,
        ),
    ]
