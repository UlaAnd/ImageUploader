from rest_framework import viewsets

from images.models import Image
from images.serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

    # Add the basename for the viewset
    basename = 'image'


    def get_queryset(self):
        # Get the currently logged-in user's profile
        user_profile = self.request.user

        # Filter images based on the user's profile
        queryset = Image.objects.filter(owner=user_profile)

        return queryset

