from django.urls import path
from django.views.generic.base import TemplateView
from tracker.views import RegisterView, AddPrescriptionView, DashboardView

app_name = 'tracker'

urlpatterns = [
    path('', TemplateView.as_view(template_name='tracker/index.html'), name='home'),
    path('register', RegisterView.as_view(), name='register'),
    path('add', AddPrescriptionView.as_view(), name='add'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

]