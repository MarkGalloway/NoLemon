# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classified',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('price', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_closed', models.DateTimeField(null=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('address', models.ForeignKey(related_name='classifieds', to='core.Address')),
            ],
        ),
        migrations.CreateModel(
            name='ClassifiedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('order', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('classified', models.ForeignKey(to='classifieds.Classified')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('image', models.ImageField(upload_to='')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='classifiedimage',
            name='image',
            field=models.ForeignKey(to='classifieds.Image'),
        ),
        migrations.AddField(
            model_name='classified',
            name='image',
            field=models.ManyToManyField(through='classifieds.ClassifiedImage', to='classifieds.Image', related_name='classifieds'),
        ),
        migrations.AddField(
            model_name='classified',
            name='seller',
            field=models.ForeignKey(related_name='classifieds', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classified',
            name='vehicle',
            field=models.ForeignKey(related_name='classifieds', to='vehicles.Vehicle'),
        ),
    ]
