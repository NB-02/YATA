# Generated by Django 4.0.2 on 2022-06-06 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0144_faction_posterperkscurrent_faction_posterperkspeace_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faction',
            name='posterWar',
        ),
    ]