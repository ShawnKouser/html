# Generated by Django 2.1.2 on 2018-10-29 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20181025_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AddField(
            model_name='post',
            name='target_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
