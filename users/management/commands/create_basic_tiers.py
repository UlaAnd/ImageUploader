from typing import Any

from django.core.management.base import BaseCommand

from users.models import Tier, TierOptions


class Command(BaseCommand):
    help = "Create basic Tries and TriesOptions objects"

    def handle(self, *args: Any, **options: Any) -> None:
        height200 = TierOptions.objects.create(height=200)
        height400 = TierOptions.objects.create(height=400)
        basic_tier = Tier.objects.create(name="Basic")
        premium_tier = Tier.objects.create(
            name="Premium", originally_uploaded_image=True
        )
        enterprise = Tier.objects.create(
            name="Enterprise", originally_uploaded_image=True, allow_fetch_expired=True
        )

        basic_tier.tier_options.add(height200)
        premium_tier.tier_options.add(height200, height400)
        enterprise.tier_options.add(height200, height400)
        self.stdout.write(self.style.SUCCESS("Objects created successfully"))
