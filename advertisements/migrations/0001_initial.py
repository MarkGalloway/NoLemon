# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('price', models.DecimalField(max_digits=11, decimal_places=2)),
                ('is_active', models.BooleanField(default=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_closed', models.DateTimeField(null=True)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AdvertisementImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('order', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('advertisement', models.ForeignKey(to='advertisements.Advertisement')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='advertisementimage',
            name='image',
            field=models.ForeignKey(to='advertisements.Image'),
        ),
    ]
