# Generated by Django 2.2.3 on 2020-01-29 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_churchadverts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='churchadverts',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'ChurchAdverts'},
        ),
        migrations.RemoveField(
            model_name='churchadverts',
            name='slug',
        ),
    ]
