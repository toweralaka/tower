from django.contrib import admin
from tracker.models import Prescription, PrescriptionUser
# Register your models here.


admin.site.register(Prescription)
admin.site.register(PrescriptionUser)