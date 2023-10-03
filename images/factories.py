
import factory
from factory.django import DjangoModelFactory

from images.models import Image


class ImageFactory(DjangoModelFactory):
    owner = factory.SubFactory("users.factories.UserProfileFactory")

    class Meta:
        model = Image

    file = factory.django.ImageField(
        filename='test_image.jpg',
        color='blue',
        width=640,
        height=480,
    )
