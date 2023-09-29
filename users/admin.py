from django.contrib import admin

from users.models import UserProfile


class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "account_tier", ]


admin.site.register(UserProfile, UserProfilesAdmin)

