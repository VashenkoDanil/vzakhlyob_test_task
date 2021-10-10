from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),
    path('account/', include('apps.account.urls')),
    path('story/', include('apps.story.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
