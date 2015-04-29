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
            name='Coll',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='colls')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.URLField(blank=True)),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('coll', models.ForeignKey(to='colls.Coll', related_name='items')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='coll',
            unique_together=set([('name', 'user')]),
        ),
    ]
