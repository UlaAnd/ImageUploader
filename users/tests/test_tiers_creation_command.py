import pytest

from users.management.commands.create_basic_tiers import Command
from users.models import Tier


@pytest.mark.django_db(True)
class TestTiersCreation:
    def test_tiers_create_command(self):
        command = Command()
        command.handle()
        tiers_amount = Tier.objects.count()
        assert tiers_amount == 3
