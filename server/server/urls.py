from django.contrib import admin
from django.urls import path
from .views import ReactAppProxyView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ReactAppProxyView.as_view(), name='react_app_proxy'),
    
]
