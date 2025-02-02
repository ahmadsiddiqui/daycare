import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.conf import settings
from studentImages.models import Image
from django.core.files.storage import default_storage
from account.models import Account, MyAccountManager

class ImageModelTests(TestCase):
    def setUp(self):
        # Create a temporary image file for testing
        self.image_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'file_content',
            content_type='image/jpeg'
        )

        # Create an Image instance
        self.image_instance = Image.objects.create(
            title='Test Image',
            account=Account.objects.create_user(email="johndoe@example.com", password="password123"),
            image=os.join(base_dir,self.image_file),
        )

    def test_image_creation(self):
        """Test that the Image instance is created correctly."""
        self.assertEqual(self.image_instance.title, 'Test Image')
        self.assertIsNotNone(self.image_instance.image)
        self.assertIsNotNone(self.image_instance.thumbnail)

    def test_image_deletion_removes_files(self):
        """Test that deleting the Image instance removes the image and thumbnail files."""
        image_file_path = self.image_instance.image.name
        thumbnail_file_path = self.image_instance.thumbnail.name

        # Store the files' paths before deletion
        self.image_instance.delete()

        # Check that the original image file has been deleted
        self.assertFalse(default_storage.exists(image_file_path))
        # Check that the thumbnail file has been deleted
        self.assertFalse(default_storage.exists(thumbnail_file_path))

    def tearDown(self):
        # Clean up any created files if they exist
        if default_storage.exists(self.image_instance.image.name):
            default_storage.delete(self.image_instance.image.name)
        if default_storage.exists(self.image_instance.thumbnail.name):
            default_storage.delete(self.image_instance.thumbnail.name)