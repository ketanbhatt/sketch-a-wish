# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saw', '0013_auto_20150217_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='progress',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
