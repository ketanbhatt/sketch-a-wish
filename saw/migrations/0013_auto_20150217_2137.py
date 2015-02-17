# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saw', '0012_wish_sketched'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='sketched',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='total_sketched',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='total_wished',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
