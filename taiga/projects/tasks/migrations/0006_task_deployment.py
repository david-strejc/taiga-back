# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_remove_deployment_task'),
        ('tasks', '0005_auto_20150114_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deployment',
            field=models.ForeignKey(blank=True, default=None, to='projects.Deployment', null=True),
            preserve_default=True,
        ),
    ]
