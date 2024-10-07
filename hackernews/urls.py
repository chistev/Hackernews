from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('comments/', include('comments.urls')),
    path('ask/', include('ask.urls')),
    path('show/', include('show.urls')),
]

# Serve static files during development
if settings.DEBUG:  # Only serve static and media files in development mode
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
