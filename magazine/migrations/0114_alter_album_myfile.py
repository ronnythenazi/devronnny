# Generated by Django 3.2.8 on 2023-07-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0113_alter_profile_familial_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='myfile',
            field=models.ImageField(blank=True, upload_to='album/%Y/%m/%d'),
        ),
    ]
