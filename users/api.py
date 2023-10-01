from rest_framework import viewsets

from users.models import Tier
from users.serializers import TierSerializer


class TierViewSet(viewsets.ModelViewSet):
    serializer_class = TierSerializer
    queryset = Tier.objects.all()
