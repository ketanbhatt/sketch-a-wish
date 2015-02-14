# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saw', '0005_auto_20150214_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sketch',
            name='submitted_on',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
