# Generated by Django 3.1.7 on 2021-03-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0006_contactteam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactteam',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
