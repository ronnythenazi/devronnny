# Generated by Django 3.2.8 on 2023-08-29 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatMsgNotification',
        ),
    ]
