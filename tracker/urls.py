from django.urls import path
from django.views.generic.base import TemplateView

from tracker.views import (AddPrescriptionView, DashboardView, RegisterView,
                           UpdatePrescriptionView, discard_reminder,
                           prescription_reminder, use_reminder)

app_name = 'tracker'

urlpatterns = [
    path(
        '', TemplateView.as_view(template_name='tracker/index.html'),
        name='home'),
    path(
        'register', RegisterView.as_view(), name='register'),
    path('add', AddPrescriptionView.as_view(), name='add'),
    path('update/<int:pk>', UpdatePrescriptionView.as_view(), name='update'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('reminder/<int:pk>/', prescription_reminder, name='reminder'),
    path(
        'reminder_discard/<int:pk>/', discard_reminder,
        name='reminder-discard'),
    path('reminder_use/<int:pk>/', use_reminder, name='reminder-use')

]
