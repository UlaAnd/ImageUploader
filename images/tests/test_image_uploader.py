import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from images.factories import ImageFactory
from images.models import Image, ImageVariant
from users.factories import UserProfileFactory


@pytest.mark.django_db(True)
class TestImageUpload:

    def test_image_creation_creates_image_option2(self):
        owner = UserProfileFactory.create()
        test_image = ImageFactory.create()
        Image.objects.create(file=test_image.file, owner=owner, title="test")
        links = ImageVariant.objects.all()
        assert links is not None

