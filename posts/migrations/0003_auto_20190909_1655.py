# Generated by Django 2.1.5 on 2019-09-09 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190909_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='p_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='u_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
