from django.contrib import admin

from users.models import UserProfile, Tier


class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "tier", ]


class TierAdmin(admin.ModelAdmin):
    list_display = ["id", "name", ]


admin.site.register(UserProfile, UserProfilesAdmin)
admin.site.register(Tier, TierAdmin)
