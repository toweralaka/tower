from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, TemplateView, View
from django.views.generic.edit import CreateView, UpdateView

from tracker.forms import PrescriptionForm, RegisterForm
from tracker.models import Prescription, PrescriptionReminder

User = get_user_model()
    

# Create your views here.

class RegisterView(View):
    success_url = '/tracker/dashboard/'

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'tracker/register.html', {'form': form})
        
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            new_user.set_password(raw_password)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(self.success_url)
        return render(request, 'tracker/register.html', {'form': form})


class AddPrescriptionView(LoginRequiredMixin, CreateView):
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"
    model = Prescription
    template_name = 'tracker/add_prescription.html'
    form_class = PrescriptionForm
    success_url = '/tracker/dashboard/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdatePrescriptionView(LoginRequiredMixin, UpdateView):
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"
    model = Prescription
    template_name = 'tracker/update_prescription.html'
    form_class = PrescriptionForm
    success_url = '/tracker/dashboard/'



class DashboardView(LoginRequiredMixin, ListView):
    login_url = "/accounts/login/"
    template_name = 'tracker/dashboard.html'
    model = Prescription

    def get_queryset(self):
        return Prescription.objects.filter(user=self.request.user)
    

@login_required
def prescription_reminder(request, pk):
    reminder = get_object_or_404(PrescriptionReminder, pk=pk)
    if request.user != reminder.prescription.user:
        return HttpResponseRedirect(reverse("tracker:dashboard"))
    reminder.administer()
    return render(request, 'tracker/reminder.html', {"reminder": reminder})

@login_required
def use_reminder(request, pk):
    reminder = get_object_or_404(PrescriptionReminder, pk=pk)
    if request.user != reminder.prescription.user:
        return HttpResponseRedirect(reverse("tracker:dashboard"))
    reminder.administer()
    return HttpResponseRedirect(
        reverse("tracker:reminder", args=(reminder.id,)))

@login_required
def discard_reminder(request, pk):
    reminder = get_object_or_404(PrescriptionReminder, pk=pk)
    if request.user != reminder.prescription.user:
        return HttpResponseRedirect(reverse("tracker:dashboard"))
    reminder.discard()
    return HttpResponseRedirect(
        reverse("tracker:reminder", args=(reminder.id,)))