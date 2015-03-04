# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saw', '0021_auto_20150302_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='sketch',
            name='sketcher',
            field=models.ForeignKey(related_name='sketcher_of_sketch', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sketch',
            name='wisher',
            field=models.ForeignKey(related_name='wisher_of_sketch', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wish',
            name='sketcher',
            field=models.ForeignKey(related_name='sketcher_of_wish', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wish',
            name='wisher',
            field=models.ForeignKey(related_name='wisher_of_wish', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
