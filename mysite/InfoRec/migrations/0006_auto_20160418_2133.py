# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoRec', '0005_auto_20160418_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myarticle',
            name='abstract',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='myarticle',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='myarticle',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='myarticle',
            name='tag',
            field=models.CharField(max_length=256, blank=True),
        ),
        migrations.AlterField(
            model_name='myarticle',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]
