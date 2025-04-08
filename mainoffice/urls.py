from django.urls import path
from . import views


urlpatterns = [
    path("base",views.base,name="base"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("privacy_policy",views.privacy_policy,name="privacy_policy"),
    path("terms",views.terms,name="terms")
]
