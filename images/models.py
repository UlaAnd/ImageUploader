import os
import sys
from datetime import timedelta
from io import BytesIO
from typing import Any, List

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from PIL import Image as PILImage

from users.models import TierOptions


class Image(models.Model):
    file = models.ImageField(upload_to="images/", blank=True)
    title = models.CharField(max_length=255)
    owner = models.ForeignKey("users.UserProfile", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    seconds = models.IntegerField(
        default=500,
        validators=[
            MinValueValidator(limit_value=300),
            MaxValueValidator(limit_value=30000),
        ],
    )

    def save(self, **kwargs: Any) -> None:
        is_adding = self._state.adding
        if is_adding:
            super().save()
            for option in self.owner.tier.tier_options.all():
                self.create_image_variant(option)
            if self.owner.tier.allow_originally_size_image:
                ImageVariant.objects.create(
                    thumbnail=self.file, image=self, variant_name="originally size"
                )
                if self.owner.tier.allow_fetch_expired:
                    expire_after = self.created_at + timedelta(seconds=self.seconds)
                    ImageVariant.objects.create(
                        thumbnail=self.file,
                        image=self,
                        expire_after=expire_after,
                        variant_name="expiring link",
                    )
            super(Image, self).save()

    def create_image_variant(self, option: TierOptions) -> None:
        height = option.height
        output_thumb = BytesIO()
        img = PILImage.open(self.file.path)
        width_percent = height / float(img.size[1])
        width = int((float(img.size[0]) * float(width_percent)))
        output_size = (width, height)
        img.thumbnail(output_size)
        # Determine the original image format
        original_format = img.format.lower()

        # Save the image in the same format as the original
        img.save(output_thumb, format=original_format, optimize=True)
        output_thumb.seek(0)

        img_name, ext = os.path.splitext(self.file.name)
        thumbnail = InMemoryUploadedFile(
            output_thumb,
            "ImageField",
            f"{img_name}_thumb{ext}",  # Preserve the original file extension
            f"image/{original_format}",  # Set the MIME type based on the original format
            sys.getsizeof(output_thumb),
            None,
        )
        variant_name = f"height {option.height} px"
        ImageVariant.objects.create(thumbnail=thumbnail, image=self, option=option, variant_name=variant_name)

    @property
    def thumbnails(self) -> List:
        return [self.imagevariant_set.all()]


class ImageVariant(models.Model):
    image = models.ForeignKey("images.Image", on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="thumbnail/", blank=True)
    option = models.ForeignKey(
        "users.TierOptions", on_delete=models.CASCADE, blank=True, null=True
    )
    variant_name = models.CharField(max_length=255)
    expire_after = models.DateTimeField(blank=True, null=True)
