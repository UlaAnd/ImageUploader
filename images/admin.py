from django.contrib import admin

from images.models import Image


class ImageAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = [
        "id",
        "file",
        "title",
        "owner",
        "url",
        "created_at",
    ]
    list_filter = ("owner", )


admin.site.register(Image, ImageAdmin)
