# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20150418_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='creator_list',
            field=models.CharField(max_length=1000, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tvshowseason',
            name='actors_list',
            field=models.CharField(max_length=3000, blank=True),
            preserve_default=True,
        ),
    ]
