# Alexandria/Alexandria/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from primer.views import say_hello
from home import views as home_views

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('say_hello/', say_hello),
    path('home/', include('home.urls')),
    path('', home_views.home),
    path('catalog/', include('catalog.urls')),
    path('people/', include('people.urls')),
]
