# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-27 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('date_added', models.DateField(verbose_name=['%m/%d/%y'])),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='birthday',
            new_name='hired',
        ),
        migrations.AddField(
            model_name='item',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Item', to='Login.User'),
        ),
    ]
