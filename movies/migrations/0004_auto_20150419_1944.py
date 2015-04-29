# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20150419_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshowseason',
            name='slug',
            field=models.SlugField(default='0', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='creator',
            field=models.ManyToManyField(related_name='created', to='movies.Person', blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='tvshowseason',
            unique_together=set([('tvshow', 'number')]),
        ),
    ]
