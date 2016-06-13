# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnotherModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OriginalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='anothermodel',
            name='foreign_key_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='an_app.OriginalModel'),
        ),
    ]
