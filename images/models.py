from django.db import models


class Image(models.Model):
    file = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=255)
    owner = models.ForeignKey("users.UserProfile", on_delete=models.CASCADE)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

