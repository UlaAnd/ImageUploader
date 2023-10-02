from django.contrib import admin

from users.models import Tier, UserProfile, TierOptions


class UserProfilesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "tier",
    ]


class TierOptionsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "height",
    ]


class TierAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]


admin.site.register(UserProfile, UserProfilesAdmin)
admin.site.register(Tier, TierAdmin)
admin.site.register(TierOptions, TierOptionsAdmin)
