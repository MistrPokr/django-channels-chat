# Generated by Django 3.0.14 on 2021-05-25 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210522_1654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messagemodel',
            options={'ordering': ('timestamp',), 'verbose_name': 'message', 'verbose_name_plural': 'messages'},
        ),
    ]
