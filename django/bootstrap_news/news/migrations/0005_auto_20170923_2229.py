# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-23 19:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_post_posttext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='postText',
            new_name='pre_Text',
        ),
    ]
