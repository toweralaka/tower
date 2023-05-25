from django.contrib.auth import login, authenticate, get_user_model
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect

from tracker.forms import RegisterForm
from tracker.models import Prescription

User = get_user_model()
    

# Create your views here.

class RegisterView(View):
    success_url = '/dashboard/'

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
    fields = [
        'name', 'description', 'dosage', 'dosage_unit', 
        'frequency', 'frequency_period']
    success_url = '/dashboard/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.user = self.request.user
        return super().form_valid(form)

    
class DashboardView(LoginRequiredMixin, ListView):
    login_url = "/accounts/login/"
    template_name = 'tracker/dashboard.html'
    model = Prescription