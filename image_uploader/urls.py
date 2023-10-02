"""
URL configuration for image_uploader project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from image_uploader import settings
from images.api import ImageViewSet
from users.api import TierViewSet

router = routers.DefaultRouter()
router.register(r"uploader", ImageViewSet)
router.register(r"tiers", TierViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v2/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
