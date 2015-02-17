# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('saw', '0008_auto_20150216_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wish',
            name='sketcher',
        ),
        migrations.AlterField(
            model_name='wish',
            name='wisher',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
