# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
