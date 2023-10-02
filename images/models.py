from io import BytesIO
import sys

import PIL
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models


class Image(models.Model):
    file = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=255)
    owner = models.ForeignKey("users.UserProfile", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, **kwargs):
        is_adding = self._state.adding
        if is_adding:
            super().save()
            for option in self.owner.tier.tier_options.all():
                # generate_thumbnail_link(width=option)

                output_size = (option.height,option.height)
                output_thumb = BytesIO()

                img = PIL.Image.open(self.file)
                img_name = self.file.name.split('.')[0]

                if img.height > 300 or img.width > 300:
                    img.thumbnail(output_size)
                    img.save(output_thumb, format='JPEG', quality=90)
                    output_thumb.seek(0)
                    img_name = self.file.name.split('.')[0]
                    thumbnail = InMemoryUploadedFile(output_thumb, 'ImageField', f"{img_name}_thumb.jpg", 'image/jpeg', sys.getsizeof(output_thumb), None)
                    thumbnail_variant = ImageVariant.objects.create(thumbnail=thumbnail, image=self, option=option)

            super(Image, self).save()


class ImageVariant(models.Model):
    image = models.ForeignKey("images.Image", on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='thumbnail/', blank=True)
    option = models.ForeignKey("users.TierOptions", on_delete=models.CASCADE)

    def __str__(self):
        return self.image

