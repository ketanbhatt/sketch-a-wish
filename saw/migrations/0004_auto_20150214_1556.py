# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saw', '0003_auto_20150214_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sketch',
            name='sketched',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sketched',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
