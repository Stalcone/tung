# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20150419_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tvshowseason',
            name='number',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
