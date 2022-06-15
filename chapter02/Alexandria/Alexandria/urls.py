# Alexandria/Alexandria/urls.py
from django.contrib import admin
from django.urls import path

from primer.views import say_hello

urlpatterns = [
    path('admin/', admin.site.urls),

    path('say_hello/', say_hello),
]
