# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoRec', '0004_article_abstract'),
    ]

    operations = [
        migrations.CreateModel(
            name='myArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='标题', max_length=256)),
                ('abstract', models.TextField(verbose_name='摘要', blank=True)),
                ('content', models.TextField(verbose_name='内容')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('tag', models.CharField(max_length=256, verbose_name='标签', blank=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='myUser',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
