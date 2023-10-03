from rest_framework import serializers
from rest_framework.reverse import reverse

from images.models import Image, ImageVariant


class ImageVariantSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = ImageVariant
        fields = (
            "id",
            "thumbnail",
            "variant_name",
            "option",
        )

    def get_thumbnail(self, model: ImageVariant) -> str:
        image_id = model.id
        url = reverse("serve_image", kwargs={"image_id": image_id})
        host = "http://localhost:8000" # it should be reading from settings.py
        return host + url


class ImageSerializer(serializers.ModelSerializer):
    thumbnails = ImageVariantSerializer(
        many=True, read_only=True, source="imagevariant_set"
    )
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Image
        fields = (
            "id",
            "file",
            "title",
            "thumbnails",
            "owner",
            "seconds",
            "created_at",
        )

    def to_representation(self, instance: Image) -> list:
        data = super().to_representation(instance)
        data["file"] = "File not available for GET requests"
        return data
