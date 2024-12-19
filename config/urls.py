from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from website.views import base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', include(('website.urls', 'website'), namespace='website')),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('', base, name='base'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
