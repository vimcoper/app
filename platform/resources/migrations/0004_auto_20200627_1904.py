# Generated by Django 3.0.5 on 2020-06-27 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_auto_20200627_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasource',
            old_name='url',
            new_name='link',
        ),
    ]
