from typing import Any

from django.http import FileResponse, Http404
from django.utils import timezone

from images.models import ImageVariant


def serve_image(request: Any, image_id: int) -> None:
    file = ImageVariant.objects.get(pk=image_id)
    if file.expire_after and timezone.now() > file.expire_after:
        raise Http404("Image has expired")
    image_file = file.thumbnail.open("rb")

    return FileResponse(image_file, content_type="image/jpeg")
