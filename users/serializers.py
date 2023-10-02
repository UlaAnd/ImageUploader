from rest_framework import serializers

from users.models import Tier


class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = (
            "id",
            "name",
            "tier_options",
            "allow_originally_size_image",
            "allow_fetch_expired",
        )
