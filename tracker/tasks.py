from django.urls import reverse
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.management import call_command
from django.utils import timezone

from dateutil.relativedelta import relativedelta



from .models import Prescription


def send_recent_reminder():
    for i in Prescription.objects.filter(is_quitted=False):
        if i.reminder_is_recent:
            i.send_use_reminder()

