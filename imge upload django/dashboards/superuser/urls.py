from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('superuser/', views.SuperUserView.as_view(), name='superuser'),
]