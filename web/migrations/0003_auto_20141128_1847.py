# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20141128_1751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='library',
            options={'verbose_name_plural': 'Library', 'get_latest_by': 'added_on', 'ordering': ['-added_on']},
        ),
        migrations.AddField(
            model_name='library',
            name='video',
            field=models.FileField(upload_to='uploads', default='one'),
            preserve_default=False,
        ),
    ]
