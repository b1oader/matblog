# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(upload_to='images/', verbose_name='photo'),
        ),
    ]
