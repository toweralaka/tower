# Generated by Django 4.2.1 on 2023-05-25 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_education_language_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 25, 11, 35, 59, 58147, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='description',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
