# Generated by Django 3.0.1 on 2021-05-22 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
