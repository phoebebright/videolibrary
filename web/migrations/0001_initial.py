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
            name='Library',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('added_on', models.DateTimeField(auto_created=True)),
                ('ref', models.CharField(unique=True, max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, null=True, max_length=30)),
                ('added_by', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'ordering': ['-added_on'],
                'get_latest_by': 'added_on',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='library',
            name='scenarios',
            field=models.ManyToManyField(to='web.Scenario'),
            preserve_default=True,
        ),
    ]
