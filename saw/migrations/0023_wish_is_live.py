# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saw', '0022_auto_20150304_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='is_live',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
