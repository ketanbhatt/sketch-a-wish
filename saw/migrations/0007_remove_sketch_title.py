# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saw', '0006_auto_20150214_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sketch',
            name='title',
        ),
    ]
