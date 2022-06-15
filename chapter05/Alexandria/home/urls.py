# Alexandria/home/urls.py

from django.urls import path

from home import views

urlpatterns = [
    path('sample/', views.sample),
    path('about/', views.about),
]
