from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Loginn app
    path('accounts/', include('accounts.urls')),

    # User Dashboards
    path('dashboards/', include('dashboards.superuser.urls')),

    # Uploads
    path('uploads/', include('uploads.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
