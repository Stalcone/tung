# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors_list',
            field=models.CharField(blank=True, max_length=3000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='director_list',
            field=models.CharField(blank=True, max_length=1000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tvshowseason',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 4, 18, 18, 15, 44, 554726, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='starred_in', to='movies.Person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(blank=True, related_name='directed', to='movies.Person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tvshowseason',
            name='actors',
            field=models.ManyToManyField(related_name='tvshow_season_starred_in', to='movies.Person'),
            preserve_default=True,
        ),
    ]
