# Generated by Django 3.0.6 on 2020-05-26 07:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0008_auto_20200526_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
