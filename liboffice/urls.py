from django.urls import path
from . import views

urlpatterns = [
    path("",views.books,name="books"),
    # Catalog page
    path("catalog", views.catalog, name="catalog"),
    
    # Membership page
    path('membership', views.membership, name='membership'),
    
    # Library Events page
    path('library_events', views.library_events, name='library_events')
    
]