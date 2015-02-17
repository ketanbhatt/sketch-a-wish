# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saw', '0011_auto_20150217_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='sketched',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
