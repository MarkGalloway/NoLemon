# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.ForeignKey(related_name='payment_profiles', to='core.Address')),
                ('user', models.ForeignKey(related_name='payment_profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=256)),
                ('promo_code', models.IntegerField(null=True)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_active', models.BooleanField()),
                ('start_date', models.DateTimeField()),
                ('expiration_date', models.DateTimeField()),
                ('product', models.ForeignKey(related_name='promotions', to='payments.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payment_complete', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('payment_profile', models.ForeignKey(related_name='receipts', to='payments.PaymentProfile')),
                ('products', models.ManyToManyField(to='payments.Product', related_name='receipts')),
                ('user', models.ForeignKey(related_name='receipts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
