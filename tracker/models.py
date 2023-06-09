from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.


class PrescriptionUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


PERIOD = (
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
    # decimal field to allow for fractions
    dosage_unit = models.CharField(max_length=50, help_text='e.g: ml, capsule, tablet, shot')
    frequency = models.DecimalField(default=1.0, max_digits=5, decimal_places=2)
    # decimal field to allow for fractions
    frequency_period = models.CharField(max_length=7, choices=PERIOD)
    start_date = models.DateTimeField(help_text='mm/dd/yyyy')
    end_date = models.DateTimeField(help_text='mm/dd/yyyy')
    total_dosage_unit_quantity = models.IntegerField(
        help_text='How many units of the dosage unit')
    refill_reminder_quantity = models.IntegerField(
        help_text='At how many units do you want to be reminded of a refill')
    # to stop the use of the prescription
    is_quitted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def reminder_is_recent(self):
        reminder_time = self.get_next_reminder
        right_now = timezone.now()
        # check if time is within 5 minutes of reminder time
        five_minutes_before = reminder_time - relativedelta(minutes=5)
        five_minutes_after = reminder_time + relativedelta(minutes=5)
        return (right_now >= five_minutes_before) and \
            (right_now <= five_minutes_after)

    @property
    def get_next_reminder(self):
        # TODO: update function to take in frequency fraction and
        # return relativedelta integer
        the_hours = int(self.frequency) if self.frequency_period == 'hour' else 0
        the_days = int(self.frequency) if self.frequency_period == 'day' else 0
        the_weeks = int(self.frequency) if self.frequency_period == 'week' else 0
        the_months = int(self.frequency) if self.frequency_period == 'month' else 0
        old_reminders = self.prescriptionreminder_set.all()
        if old_reminders.exists():
            last_time = old_reminders.last().reminder_time
            time_increment = relativedelta(
                            hours=the_hours, days=the_days, 
                            weeks=the_weeks, month=the_months)
            new_time = last_time + time_increment
        else:
            new_time = self.start_date
        return new_time
    
    def send_use_reminder(self):
        if self.reminder_is_recent:
            if not self.is_quitted:
                current_site = Site.objects.get_current()
                new_reminder = self.prescriptionreminder_set.create(
                                    prescribed_time=self.get_next_reminder)
                reminder_link = reverse(
                    "tracker:reminder-use", args=(new_reminder.id,))
                full_link = current_site.domain + reminder_link
                the_time_formatted = self.get_next_reminder.strftime(
                    "%I:%M:%S %p, %a, %b %Y.")
                try:
                    send_mail(
                        f"{self.name.capitalize()} Prescription Use Reminder",
                        (
                            f"You are to use {self.dosage} {self.dosage_unit} of "
                            f"{self.name} at {the_time_formatted}. Confirm "
                            f"use by visiting this link {full_link}"),
                        settings.DEFAULT_FROM_EMAIL,
                        [self.user.email],
                        fail_silently=False,
                    )
                    new_reminder.is_reminded = True
                    new_reminder.save()
                except Exception:
                    pass

    @property
    def get_remainder(self):
        return self.total_dosage_unit_quantity - self.get_total_administered

    @property
    def is_refill_time(self):
        return self.get_remainder <= self.refill_reminder_quantity

    @property
    def get_total_administered(self):
        all_administration = self.prescriptionreminder_set.filter(
                                is_administered=True).count()
        
        return all_administration * self.dosage




class PrescriptionReminder(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    prescribed_time = models.DateTimeField()
    is_reminded = models.BooleanField(default=False)
    is_administered = models.BooleanField(default=False)
    reminder_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.prescription} at {self.reminder_time}'
        # is_remided={self.is_reminded}'

    def administer(self):
        self.is_administered = True
        self.save()

    def discard(self):
        self.is_administered = False
        self.save()


class PrescriptionRefill(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    refill_quantity = models.IntegerField()
    refill_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.prescription}'
