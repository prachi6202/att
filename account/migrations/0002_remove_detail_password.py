# Generated by Django 2.2.3 on 2020-08-23 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='password',
        ),
    ]
