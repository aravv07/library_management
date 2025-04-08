from django.urls import path
from . import views
from .views import register_view, login_view, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index,name="index"),
    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view')
]