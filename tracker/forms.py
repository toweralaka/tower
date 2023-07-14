from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from tracker.models import Prescription

User = get_user_model()

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email' )


class PrescriptionForm(forms.ModelForm):
    PERIOD = (
        ('-------', '-------'),
        ('hour', 'hour'),
        ('day', 'day'),
        ('week', 'week'),
        ('month', 'month'),
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        max_length=250, 
        help_text='medication name')
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        help_text='What the medication is meant for')
    dosage = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': 0.10}),
        max_digits=5, decimal_places=2)
    dosage_unit = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50, help_text='e.g: ml, capsule, tablet, shot')
    frequency = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': 0.10}),
        max_digits=5, decimal_places=2)
    frequency_period = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=PERIOD)
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'}),
        help_text='mm/dd/yyyy')
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'}),
        help_text='mm/dd/yyyy')
    total_dosage_unit_quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        help_text='how many units of the dosage_unit')
    refill_reminder_quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        help_text='At how many units do you want to be reminded of a refill')

    class Meta:
        model = Prescription
        exclude = ['user', 'track_for', 'is_quitted']
