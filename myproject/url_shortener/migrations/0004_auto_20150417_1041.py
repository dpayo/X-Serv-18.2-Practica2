# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0003_table_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='url',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
