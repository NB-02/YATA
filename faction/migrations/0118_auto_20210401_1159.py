# Generated by Django 3.1.7 on 2021-04-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0117_auto_20210323_2312'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='attackchain',
            index=models.Index(fields=['report_id', 'timestamp_ended'], name='faction_att_report__4f455b_idx'),
        ),
    ]