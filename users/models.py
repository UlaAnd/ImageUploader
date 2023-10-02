from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    tier = models.ForeignKey("users.Tier", on_delete=models.CASCADE, null=True)


class Tier(models.Model):
    name = models.CharField(max_length=255)
    tier_options = models.ManyToManyField("users.TierOptions")
    allow_originally_size_image = models.BooleanField(default=False)
    allow_fetch_expired = models.BooleanField(default=False)


class TierOptions(models.Model):
    height = models.IntegerField(default=200)
