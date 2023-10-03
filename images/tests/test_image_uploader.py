import pytest

from images.factories import ImageFactory
from images.models import Image, ImageVariant
from users.factories import UserProfileFactory
from users.management.commands.create_basic_tiers import Command
from users.models import UserProfile, Tier


@pytest.mark.django_db(True)
class TestImageUpload:

    def test_image_creation_creates_image_option(self):
        owner = UserProfileFactory.create()
        ImageFactory.create(owner=owner, title="test")
        links = ImageVariant.objects.all()
        assert links is not None

    def test_enterprise_images_creates(self):
        command = Command()
        command.handle()
        enterprise_tier = Tier.objects.get(name="Enterprise")
        owner = UserProfileFactory.create(tier=enterprise_tier)
        ImageFactory.create(owner=owner, title="test")
        links = ImageVariant.objects.count()
        assert links == 4


