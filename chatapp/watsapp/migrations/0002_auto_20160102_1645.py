# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='message',
            name='pub_date',
            field=models.DateTimeField(verbose_name='publication date'),
        ),
    ]
