import sys
from io import BytesIO
from typing import Any, List

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from PIL import Image as PILImage


class Image(models.Model):
    file = models.ImageField(upload_to="images/", blank=True)
    title = models.CharField(max_length=255)
    owner = models.ForeignKey("users.UserProfile", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs: Any) -> None:
        is_adding = self._state.adding
        if is_adding:
            super().save()
            for option in self.owner.tier.tier_options.all():
                output_size = (option.height, option.height)
                output_thumb = BytesIO()

                img = PILImage.open(self.file.path)
                img_name = self.file.name.split(".")[0]

                img.thumbnail(output_size)
                img.save(output_thumb, format="JPEG", quality=90)
                output_thumb.seek(0)
                img_name = self.file.name.split(".")[0]
                thumbnail = InMemoryUploadedFile(
                    output_thumb,
                    "ImageField",
                    f"{img_name}_thumb.jpg",
                    "image/jpeg",
                    sys.getsizeof(output_thumb),
                    None,
                )
                ImageVariant.objects.create(
                    thumbnail=thumbnail, image=self, option=option
                )

            super(Image, self).save()

    @property
    def thumbnails(self) -> List:
        return [self.imagevariant_set.all()]


class ImageVariant(models.Model):
    image = models.ForeignKey("images.Image", on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="thumbnail/", blank=True)
    option = models.ForeignKey(
        "users.TierOptions", on_delete=models.CASCADE, blank=True
    )
