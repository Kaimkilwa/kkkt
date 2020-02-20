# Generated by Django 2.2.3 on 2020-01-29 09:05

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_auto_20200110_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='dominion',
            field=models.CharField(default='Lutheran', max_length=100),
        ),
        migrations.AddField(
            model_name='platform',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='platform',
            name='region',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='platform',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]