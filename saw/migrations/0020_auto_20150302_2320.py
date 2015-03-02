# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saw', '0019_auto_20150302_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sketch',
            name='image_temp',
        ),
        migrations.AddField(
            model_name='sketch',
            name='image',
            field=models.ImageField(upload_to=b'sketches/', blank=True),
            preserve_default=True,
        ),
    ]
