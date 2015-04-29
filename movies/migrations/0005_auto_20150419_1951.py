# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20150419_1944'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tvshowseason',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='tvshowseason',
            name='slug',
        ),
    ]
