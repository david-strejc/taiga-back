# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20150114_0954'),
        ('projects', '0021_auto_20150418_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('deployment_server', models.CharField(max_length=256, blank=True)),
                ('base_git_url', models.CharField(max_length=512, blank=True)),
                ('base_branch', models.CharField(max_length=128, blank=True)),
                ('deployment_status', models.BooleanField(default=False)),
                ('task', models.ForeignKey(to='tasks.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
