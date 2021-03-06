# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 22:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cron', '0001_initial'),
        ('main', '0001_initial'),
        ('skyscannerSDK', '0002_auto_20161008_1224'),
        ('searchreports', '0001_initial'),
        ('travelrequests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outbound', models.DateField()),
                ('inbound', models.DateField()),
                ('cron', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cron.FlightSearchCronJob')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_city_request', to='skyscannerSDK.Place')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_city_request', to='skyscannerSDK.Place')),
                ('report', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='searchreports.Report')),
            ],
        ),
        migrations.AddField(
            model_name='userrequestmatch',
            name='wiuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.WanderitUser'),
        ),
        migrations.AddField(
            model_name='userrequestmatch',
            name='search_request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travelrequests.SearchRequest'),
        ),
    ]
