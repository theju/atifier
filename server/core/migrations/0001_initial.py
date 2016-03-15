# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 12:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageScrapeResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output', models.TextField(null=True)),
                ('hash', models.TextField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_on', '-created_on'],
            },
        ),
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_name', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex='[\\w\\-]+')])),
                ('url', models.URLField()),
                ('selector', models.TextField()),
                ('interval', models.PositiveIntegerField(default=5)),
                ('max_results', models.PositiveIntegerField(default=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_on', '-created_on'],
            },
        ),
        migrations.AddField(
            model_name='pagescraperesult',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.WebPage'),
        ),
    ]
