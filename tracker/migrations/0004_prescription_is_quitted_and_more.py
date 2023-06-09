# Generated by Django 4.2.1 on 2023-06-14 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_prescription_total_dosage_unit_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='is_quitted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='prescription',
            name='refill_reminder_quantity',
            field=models.IntegerField(default=5, help_text='At how many units do you want to be reminded of a refill'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prescription',
            name='end_date',
            field=models.DateTimeField(help_text='mm/dd/yyyy'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='frequency_period',
            field=models.CharField(choices=[('hour', 'hour'), ('day', 'day'), ('week', 'week'), ('month', 'month')], max_length=7),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='start_date',
            field=models.DateTimeField(help_text='mm/dd/yyyy'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='total_dosage_unit_quantity',
            field=models.IntegerField(help_text='How many units of the dosage unit'),
        ),
        migrations.CreateModel(
            name='PrescriptionReminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_reminded', models.BooleanField(default=False)),
                ('is_administered', models.BooleanField(default=False)),
                ('reminder_time', models.DateTimeField(auto_now_add=True)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='PrescriptionRefill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refill_quantity', models.IntegerField()),
                ('refill_date', models.DateTimeField(auto_now_add=True)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.prescription')),
            ],
        ),
    ]
