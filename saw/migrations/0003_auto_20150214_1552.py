# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saw', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='sketch',
            name='sketched',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wish',
            name='locked',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
