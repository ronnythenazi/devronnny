# Generated by Django 2.0.7 on 2021-09-30 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210928_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
