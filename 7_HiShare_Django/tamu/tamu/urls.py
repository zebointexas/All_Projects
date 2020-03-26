from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #  path('admin/', admin.site.urls),
    #   path('pig/', include('pig.urls')),

        url(r'^admin/', admin.site.urls),
        url(r'^pig/', include('pig.urls')),

]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



