# Generated by Django 3.2.8 on 2021-12-24 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0028_alter_blogpost_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumb',
            field=models.ImageField(upload_to=''),
        ),
    ]
