# Generated by Django 4.0.2 on 2022-04-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0141_remove_faction_memberstatus_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attacksreport',
            name='wall',
        ),
        migrations.AddField(
            model_name='attacksreport',
            name='war',
            field=models.TextField(default='{}'),
        ),
        migrations.DeleteModel(
            name='Wall',
        ),
    ]
