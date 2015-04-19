# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20150114_0954'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0019_auto_20150311_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', djorm_pgarray.fields.TextArrayField(verbose_name='tags', dbtype='text')),
                ('version', models.IntegerField(verbose_name='version', default=1)),
                ('is_blocked', models.BooleanField(verbose_name='is blocked', default=False)),
                ('blocked_note', models.TextField(verbose_name='blocked note', default='', blank=True)),
                ('server', models.CharField(max_length=30)),
                ('base_git_url', models.CharField(max_length=30)),
                ('base_branch', models.CharField(max_length=30)),
                ('deployment_status', models.CharField(max_length=30)),
                ('task', models.ForeignKey(to='tasks.Task', verbose_name='project', related_name='tasks')),
                ('watchers', models.ManyToManyField(verbose_name='watchers', blank=True, to=settings.AUTH_USER_MODEL, null=True, related_name='projects_deployment+')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
