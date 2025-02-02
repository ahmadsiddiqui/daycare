from django.test import TestCase, Client
from django.urls import reverse
from account.models import Account, 
from studentVaccinations.models import Vaccination, VaccinationRecord
from studentVaccinations.forms import RecordVaccinationFormAdmin

class RecordVaccinationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = Account.objects.create_user(email=admin@example.com, password='adminpass', is_admin=True)
        self.regular_user = Account.objects.create_user(email='user@example.com', password='userpass', is_admin=False)
        self.admin_user.is_admin= True
        self.regular_user.is_admin= False

        self.vaccine = Vaccination.objects.create(name='Flu Vaccine')

    def test_redirect_if_unauthenticated(self):
        response = self.client.get(reverse('record_vaccination'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login
        self.assertRedirects(response, reverse('login'))

    def test_record_vaccination_for_admin_get(self):
        self.client.login(email='admin@example.com', password='adminpass')
        response = self.client.get(reverse('record_vaccination'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)  # Check that the form is in context
        self.assertIn('vaccineList', response.context)  # Check that the vaccine list is in context
        self.assertIn('accountList', response.context)  # Check that the account list is in context

    def test_record_vaccination_for_admin_post_valid(self):
        self.client.login(email='admin@example.com', password='adminpass')
        response = self.client.post(reverse('record_vaccination'), {
            'account': self.regular_user.id,
            'vaccine': self.vaccine.id,
            
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful save
        self.assertRedirects(response, reverse('record_vaccination'))
        self.assertEqual(VaccinationRecord.objects.count(), 1)  # Check if record is created

    def test_record_vaccination_for_admin_post_invalid(self):
        self.client.login(email='admin@example.com', password='adminpass')
        response = self.client.post(reverse('record_vaccination'), {
            'account': '',  # Invalid data
            'vaccine': '',  # Invalid data
            
        })
        self.assertEqual(response.status_code, 200)  # Should render the form again
        self.assertIn('form', response.context)  # Check that the form is in context again
        self.assertTrue(response.context['form'].errors)  # Check that there are form errors

    def test_record_vaccination_for_regular_user(self):
        self.client.login(username='user', password='userpass')
        response = self.client.get(reverse('record_vaccination'))
        self.assertEqual(response.status_code, 403)  # Should return forbidden response
        self.assertContains(response, "Prohibited")  # Check for the prohibited message

    def tearDown(self):
        self.admin_user.delete()
        self.regular_user.delete()
        self.vaccine.delete()
