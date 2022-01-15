# Generated by Django 3.2.8 on 2022-01-15 00:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0064_auto_20220114_1555'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Moderators',
        ),
        migrations.DeleteModel(
            name='regUser',
        ),
        migrations.AddField(
            model_name='profile',
            name='birthDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='familial_status',
            field=models.CharField(blank=True, choices=[('single', 'רווק'), ('married', 'נשוי'), ('divorced', 'גרוש'), ('married_again', 'נשוי פעם נוספת')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='joinDate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mtdna',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='politic_views',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='race',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='religion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.CharField(blank=True, choices=[('male', 'גבר'), ('female', 'נקבה')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='slogan',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='y_dna',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
