# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoRec', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.RemoveField(
            model_name='article',
            name='update_time',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(max_length=256, blank=True, verbose_name='标签'),
        ),
    ]
