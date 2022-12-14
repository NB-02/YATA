# Generated by Django 4.0.2 on 2022-06-07 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0146_faction_waragainst_factiontarget'),
    ]

    operations = [
        migrations.AddField(
            model_name='factiontarget',
            name='dibs_name',
            field=models.CharField(default='player_name', max_length=16),
        ),
        migrations.AddField(
            model_name='factiontarget',
            name='dibs_tid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='factiontarget',
            name='defense',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='factiontarget',
            name='dexterity',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='factiontarget',
            name='speed',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='factiontarget',
            name='strength',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='factiontarget',
            name='total',
            field=models.BigIntegerField(default=-1),
        ),
    ]
