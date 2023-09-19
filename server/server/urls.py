from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("/encrypt", views.encryptData, name='encrypt_data'),
]
