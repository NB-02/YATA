# Generated by Django 4.0.2 on 2022-06-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0149_faction_upgradetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='factiontarget',
            name='revivable',
            field=models.BooleanField(default=0),
        ),
    ]
