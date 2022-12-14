# Generated by Django 3.1.5 on 2021-06-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0137_remove_chain_attacks_last_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='factiondata',
            name='crontabs_armory_live',
            field=models.TextField(default='[1]'),
        ),
        migrations.AddField(
            model_name='factiondata',
            name='crontabs_armory_report',
            field=models.TextField(default='[2]'),
        ),
        migrations.AddField(
            model_name='factiondata',
            name='crontabs_attacks_live',
            field=models.TextField(default='[1,2]'),
        ),
        migrations.AddField(
            model_name='factiondata',
            name='crontabs_attacks_report',
            field=models.TextField(default='[3]'),
        ),
        migrations.AddField(
            model_name='factiondata',
            name='crontabs_chain_live',
            field=models.TextField(default='[1,2,3,4]'),
        ),
        migrations.AddField(
            model_name='factiondata',
            name='crontabs_chain_report',
            field=models.TextField(default='[5]'),
        ),
        migrations.AddField(
            model_name='factiondata',
            name='crontabs_revives_live',
            field=models.TextField(default='[1]'),
        ),
        migrations.AddField(
            model_name='factiondata',
            name='crontabs_revives_report',
            field=models.TextField(default='[2]'),
        ),
    ]
