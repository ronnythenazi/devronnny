# Generated by Django 3.2.8 on 2023-07-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0111_alter_profile_nick'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bestEvent',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='fantasy',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='hate',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='hobby',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='love',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nightmare',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='worstEvent',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]