from django.contrib import admin # noqa

from tracker.models import Prescription, PrescriptionReminder, PrescriptionUser

# Register your models here.


admin.site.register(Prescription)
admin.site.register(PrescriptionReminder)
admin.site.register(PrescriptionUser)
