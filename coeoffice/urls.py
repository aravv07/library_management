# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('fiction', views.fiction, name='fiction'),
    path('Non_fiction', views.Non_fiction, name='Non_fiction'),
    path('Comics', views.Comics, name='Comics'),
    path('Romance', views.Romance, name='Romance')
]
