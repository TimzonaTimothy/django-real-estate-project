# Generated by Django 3.0.1 on 2021-05-22 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_sold',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
