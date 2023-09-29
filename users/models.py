from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    TYPE_BASIC = "basic"
    TYPE_PREMIUM = "premium"
    TYPE_ENTERPRISE = "enterprise"
    TYPE_CHOICES = (
        (TYPE_BASIC, "Basic"),
        (TYPE_PREMIUM, "Premium"),
        (TYPE_ENTERPRISE, "Enterprise"),
    )
    email = models.EmailField("email address", blank=True, null=True)
    account_tier = models.CharField(max_length=20, choices=TYPE_CHOICES, default=TYPE_BASIC)

