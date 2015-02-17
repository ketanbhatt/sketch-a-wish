# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saw', '0007_remove_sketch_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='sketcher',
            field=models.ForeignKey(related_name='sketcher', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wish',
            name='wisher',
            field=models.ForeignKey(related_name='wisher', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
