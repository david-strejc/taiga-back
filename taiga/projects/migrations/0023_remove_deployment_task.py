# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_deployment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deployment',
            name='task',
        ),
    ]
