# Alexandria/Alexandria/urls.py
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic.base import RedirectView

import debug_toolbar

from primer.views import say_hello
from home import views as home_views

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),

    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('say_hello/', say_hello),
    path('home/', include('home.urls')),
    path('', home_views.home),
    path('catalog/', include('catalog.urls')),
    path('people/', include('people.urls')),
    path('review/', include('review.urls')),

    path('__debug__/', include(debug_toolbar.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
