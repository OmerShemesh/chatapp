# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watsapp', '0002_auto_20160102_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_text',
            field=models.TextField(max_length=200),
        ),
    ]
