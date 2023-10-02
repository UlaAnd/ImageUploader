from rest_framework import viewsets

from images.models import Image, ImageVariant
from images.serializers import ImageSerializer, ImageVariantSerializer


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    basename = "image"

    def get_queryset(self):
        user_profile = self.request.user
        queryset = Image.objects.filter(owner=user_profile)
        return queryset


class ImageVariantViewSet(viewsets.ModelViewSet):
    serializer_class = ImageVariantSerializer
    queryset = ImageVariant.objects.all()
