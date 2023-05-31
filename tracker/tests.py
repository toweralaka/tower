from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.test.utils import setup_test_environment, teardown_test_environment
from django.urls import reverse

from .models import Prescription, PrescriptionUser

User = get_user_model()

# Create your tests here.

class PrescriptionUserModelTests(TestCase):
    def test_model_str_returns_name(self):
        new_prescription_user = PrescriptionUser(name='person')
        self.assertEqual(new_prescription_user.__str__(), 'person')


class PrescriptionModelTests(TestCase):
    def test_model_str_returns_name(self):
        new_prescription = Prescription(name='medicine')
        self.assertEqual(new_prescription.__str__(), 'medicine')


class DashboardView(TestCase):
    def setUp(self):
        self.new_user = User.objects.create(username='phil')
        self.new_user.set_password('secret')
        self.new_user.save()

    def test_unauthenticated_dashboard_view_redirect(self):
        response = self.client.get(reverse("tracker:dashboard"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")

    def test_authenticated_dashboard_view(self):
        c = self.client
        c.force_login(self.new_user)
        response = c.get(reverse("tracker:dashboard"))
        self.assertContains(response, "Add New")

    def test_no_prescriptions(self):
        c = self.client
        c.force_login(self.new_user)
        response = self.client.get(reverse("tracker:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You do not have prescriptions.")


class RegisterViewTest(TestCase):
    def setUp(self):
        self.num_users = User.objects.count()

    def test_register_new_user(self):
        response = self.client.post(reverse("tracker:register"), 
        data={
            'username': 'person',
            'password1': 'secret',
            'password2': 'secret',
            'first_name': 'myfirst',
            'last_name': 'mylast',
            'email': 'myfirst@example.com',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracker/register.html')

    def test_register_password_mismatch_unsuccessful(self):
        response = self.client.post(reverse("tracker:register"), 
        data={
            'username': 'person',
            'password1': 'secret',
            'password2': 'secret1',
            'first_name': 'myfirst',
            'last_name': 'mylast',
            'email': 'myfirst@example.com',
        })
        self.assertContains(response, "The two password fields")


class AddPrescriptionViewTest(TestCase):
    def setUp(self):
        self.new_user = User.objects.create(username='phil')
        self.new_user.set_password('secret')
        self.new_user.save()
    
    def test_unauthenticated_add_prescriptions_redirected(self):
        response = self.client.post(reverse("tracker:add"), 
        data={
            'name': 'paracetamol', 
            'description': 'for headache', 
            'dosage': 1, 
            'dosage_unit': 'tablet', 
            'frequency': 3, 
            'frequency_period': 'daily', 
            'start_date': '01/20/2023', 
            'end_date': '02/20/2023'
            }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login')
        
    def test_add_prescriptions(self):
        c = self.client
        c.force_login(self.new_user)
        response = self.client.post(reverse("tracker:add"), 
        data={
            'name': 'paracetamol', 
            'description': 'for headache', 
            'dosage': 1, 
            'dosage_unit': 'tablet', 
            'frequency': 3, 
            'frequency_period': 'daily', 
            'start_date': '01/20/2023', 
            'end_date': '02/20/2023'
            })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracker/add_prescription.html')
        
