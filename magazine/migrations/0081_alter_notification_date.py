# Generated by Django 3.2.8 on 2022-01-20 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0080_alter_notification_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default='20.01.2022 14:14:41'),
        ),
    ]