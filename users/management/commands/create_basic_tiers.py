from typing import Any

from django.core.management.base import BaseCommand

from users.models import Tier, TierOptions


class Command(BaseCommand):
    help = "Create basic Tries and TriesOptions objects"

    def handle(self, *args: Any, **options: Any) -> None:
        height200, created = TierOptions.objects.get_or_create(
            height=200, name="200px"
        )
        height400, created = TierOptions.objects.get_or_create(
            height=400, name="400px"
        )
        basic_tier, created = Tier.objects.get_or_create(name="Basic")
        premium_tier, created = Tier.objects.get_or_create(
            name="Premium", allow_originally_size_image=True
        )
        enterprise, created = Tier.objects.get_or_create(
            name="Enterprise", allow_originally_size_image=True, allow_fetch_expired=True
        )
        basic_tier.tier_options.add(height200)
        premium_tier.tier_options.add(height200, height400)
        enterprise.tier_options.add(height200, height400)
        self.stdout.write(self.style.SUCCESS("Objects created successfully"))
