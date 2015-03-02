# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saw', '0020_auto_20150302_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sketch',
            old_name='image',
            new_name='sketch_image',
        ),
    ]
