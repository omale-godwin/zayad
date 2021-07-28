
from django import urls
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('event/', include('event.urls')), 
    path('contact/', include('contact.urls')),
    path('causes/', include('causes.urls')),
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

