# Generated by Django 4.0.2 on 2022-04-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0142_remove_attacksreport_wall_attacksreport_war_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attacksreport',
            name='war_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='attacksreport',
            name='war_type',
            field=models.CharField(default='Unkown', max_length=16),
        ),
    ]
