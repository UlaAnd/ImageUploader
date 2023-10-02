from rest_framework import serializers

from images.models import Image, ImageVariant


class ImageVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageVariant
        fields = (
            "id",
            "thumbnail",
            "option",
        )


class ImageSerializer(serializers.ModelSerializer):
    thumbnails = ImageVariantSerializer( read_only=True)

    class Meta:
        model = Image
        fields = (
            "id",
            "file",
            "title",
            "owner",
            "thumbnails",
            "created_at",
        )
