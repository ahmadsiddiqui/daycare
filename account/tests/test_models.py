from django.test import TestCase
from account.models import Account, MyAccountManager

class AccountModelTests(TestCase):
    def setUp(self):
        self.email = "test@example.com"
        self.password = "testpassword123"

    def test_create_user_with_email(self):
        """Test creating a user with an email is successful."""
        user = Account.objects.create_user(email=self.email, password=self.password)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertIsNotNone(user.id)  # Ensure user is saved to the database

    def test_create_user_without_email(self):
        """Test creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            Account.objects.create_user(email=None, password=self.password)
        self.assertEqual(str(context.exception), "Users must have an email address")

    def test_create_user_without_password(self):
        """Test creating a user without a password works."""
        user = Account.objects.create_user(email=self.email)
        self.assertEqual(user.email, self.email)
        self.assertIsNotNone(user.id)  # Ensure user is saved to the database
        self.assertFalse(user.check_password('wrongpassword'))  # Should not authenticate with wrong password

    def test_create_superuser(self):
        """Test creating a superuser is successful and has correct attributes."""
        superuser = Account.objects.create_superuser(email=self.email, password=self.password)
        
        # Assert that the superuser's email is correct
        self.assertEqual(superuser.email, self.email)
        
        # Assert that the password is set correctly
        self.assertTrue(superuser.check_password(self.password))
        
        # Assert that the superuser has admin, staff, and superuser flags set to True
        self.assertTrue(superuser.is_admin)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        
        # Ensure user is saved to the database
        self.assertIsNotNone(superuser.id)

    def test_create_superuser_without_email(self):
        """Test creating a superuser without an email raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            Account.objects.create_superuser(email=None, password=self.password)
        self.assertEqual(str(context.exception), "Users must have an email address")

    def test_create_superuser_without_password(self):
        """Test creating a superuser without a password raises an error."""
        with self.assertRaises(ValueError) as context:
            Account.objects.create_superuser(email=self.email, password='')
        self.assertEqual(str(context.exception), "Superusers must have a password.")