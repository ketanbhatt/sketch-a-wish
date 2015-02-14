# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saw', '0004_auto_20150214_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sketch',
            old_name='created_on',
            new_name='assigned_on',
        ),
        migrations.AddField(
            model_name='sketch',
            name='submitted_on',
            field=models.DateTimeField(default=None),
            preserve_default=True,
        ),
    ]
