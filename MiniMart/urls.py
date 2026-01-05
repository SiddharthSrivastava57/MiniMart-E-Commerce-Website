
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),  # Shop URLs at root
    path('accounts/', include('accounts.urls')),  # Custom auth URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth (login/logout)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)