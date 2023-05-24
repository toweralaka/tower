from django.conf import settings
from django.db import models

# Create your models here.


class PrescriptionUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

PERIOD = (
    ('second', 'second'),
    ('minute', 'minute'),
    ('hour', 'hour'),
    ('day', 'day'),
    ('week', 'week'),
    ('month', 'month'),
)
class Prescription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE)
    track_for = models.ForeignKey(
        PrescriptionUser, 
        on_delete=models.SET_NULL, 
        null=True, blank=True)
    name = models.CharField(max_length=250, help_text='medication name')
    description = models.TextField(
        blank=True, null=True, help_text='What the medication is meant for')
    dosage = models.DecimalField(default=1.0, max_digits=5, decimal_places=2)
    #decimal field to allow for fractions
    dosage_unit = models.CharField(max_length=50)
    frequency = models.DecimalField(default=1.0, max_digits=5, decimal_places=2)
    #decimal field to allow for fractions
    frequency_period = models.CharField(max_length=7, choices=PERIOD)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
