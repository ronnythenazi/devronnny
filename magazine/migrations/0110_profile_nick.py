# Generated by Django 3.2.8 on 2023-07-05 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0109_auto_20230630_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nick',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]