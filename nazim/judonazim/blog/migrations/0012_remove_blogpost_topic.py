# Generated by Django 2.0.7 on 2021-09-30 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20211001_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='topic',
        ),
    ]
