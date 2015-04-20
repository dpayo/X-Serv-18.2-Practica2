# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0002_remove_table_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='key',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
