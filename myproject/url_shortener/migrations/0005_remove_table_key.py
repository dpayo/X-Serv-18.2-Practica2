# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0004_auto_20150417_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='key',
        ),
    ]
