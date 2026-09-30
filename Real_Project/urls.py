from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('registration/', include('registration.urls')),
    path('about/', include('about.urls')),
    path('contactus/', include('contactus.urls')),
    path('property/', include('property.urls')),
    path('shop/', include('shop.urls')),

]
urlpatterns += [
    re_path(
        r'^media/(?P<path>.*)$',
        serve,
        {
            'document_root': settings.MEDIA_ROOT,
        },
    ),
]
