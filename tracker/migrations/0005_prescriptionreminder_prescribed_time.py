# Generated by Django 4.2.1 on 2023-06-14 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_prescription_is_quitted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriptionreminder',
            name='prescribed_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 14, 18, 29, 44, 436125, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
