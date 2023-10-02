import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from images.models import Image, ImageVariant
from users.factories import UserProfileFactory



@pytest.mark.django_db(True)
class TestImageApiUpload(APITestCase):
    def test_image_creation_creates_image_option(self):
        owner = UserProfileFactory.create()
        upload_to_path = Image._meta.get_field("file").upload_to

        image_file = SimpleUploadedFile(
            "test_image.jpg", b"content", content_type="image/jpeg"
        )
        files = {"file": ("test_image.jpg", image_file)}

        payload = {
            "title": "Test Image",
            "owner": owner.id,
        }
        url = reverse("image-list")
        self.client.post(url, data=payload, files=files)
        links = ImageVariant.objects.all()
        assert links is not None
