from rest_framework import serializers

from images.models import Image, ImageVariant


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            "id",
            "file",
            "title",
            "owner",
            "created_at",
        )


class ImageVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageVariant
        fields = ("id",)
