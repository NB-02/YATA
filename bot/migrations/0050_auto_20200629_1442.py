# Generated by Django 3.0.4 on 2020-06-29 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0049_bot_server'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='serverId',
            new_name='server_id',
        ),
    ]