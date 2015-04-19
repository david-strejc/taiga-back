# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_deployment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deployment',
            name='task',
        ),
        migrations.RemoveField(
            model_name='deployment',
            name='watchers',
        ),
        migrations.DeleteModel(
            name='Deployment',
        ),
    ]
