import os
from django.test import TestCase
from django.urls import reverse
from django.core.files import File

class RegistrationRequestViewTests(TestCase):
    def setUp(self):
        self.url = reverse('register_request')  
        self.test_file_path = 'request_file.csv'

    def tearDown(self):
        # Remove the test file if it exists
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_registration_request_view_post(self):
        """Test that the registration_request_view handles POST requests correctly."""
        # Simulate a POST request with name and email
        response = self.client.post(self.url, {
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        })

        # Check that the response is a render of the correct template
        self.assertTemplateUsed(response, 'account/register_request.html')

        # Verify that the data was written to the file
        with open(self.test_file_path, 'r') as f:
            content = f.read().strip()

        expected_content = "John Doe,john.doe@example.com"
        self.assertEqual(content, expected_content)

    def test_registration_request_view_get(self):
        """Test that the registration_request_view handles GET requests correctly."""
        response = self.client.get(self.url)

        # Check that the response is a render of the correct template
        self.assertTemplateUsed(response, 'account/register_request.html')
