# Generated by Django 4.2.1 on 2023-06-02 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_education_still_in_progress_experience_is_seasonal_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='discipline',
            new_name='course',
        ),
    ]