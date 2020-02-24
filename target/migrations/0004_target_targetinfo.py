# Generated by Django 3.0.1 on 2020-02-17 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0035_player_attacksupda'),
        ('target', '0003_attack'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_id', models.IntegerField(default=0)),
                ('name', models.CharField(default='attacker_name', max_length=16)),
                ('rank', models.CharField(default='rank', max_length=32)),
                ('level', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('update_timestamp', models.IntegerField(default=0)),
                ('life_current', models.IntegerField(default=0)),
                ('life_maximum', models.IntegerField(default=0)),
                ('last_action_timestamp', models.IntegerField(default=0)),
                ('last_action_relative', models.CharField(blank=True, default='last_action_relative', max_length=32, null=True)),
                ('status_description', models.CharField(blank=True, default='last_action_relative', max_length=32, null=True)),
                ('status_details', models.CharField(blank=True, default='last_action_relative', max_length=32, null=True)),
                ('status_state', models.CharField(blank=True, default='last_action_relative', max_length=32, null=True)),
                ('status_until', models.IntegerField(default=0)),
                ('faction_position', models.CharField(default='faction_position', max_length=16)),
                ('faction_name', models.CharField(default='faction_name', max_length=32)),
                ('faction_faction_id', models.IntegerField(default=0)),
                ('faction_faction_dif', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TargetInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_id', models.IntegerField(default=0)),
                ('update_timestamp', models.IntegerField(default=0)),
                ('last_attack_timestamp', models.IntegerField(default=0)),
                ('fairFight', models.FloatField(default=0)),
                ('baseRespect', models.FloatField(default=0)),
                ('flatRespect', models.FloatField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.Player')),
            ],
        ),
    ]