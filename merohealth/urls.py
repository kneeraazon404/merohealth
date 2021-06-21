from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
    path("accounts/", include("accounts.urls")),
    path("lab/", include("lab.urls")),
    path("verification/", include("verify_email.urls")),
    path("accounts/", include("allauth.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
