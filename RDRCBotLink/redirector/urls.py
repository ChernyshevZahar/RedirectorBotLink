from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/get/', views.get_link, name='get_link'),
    path('get-utms/', views.get_urls, name='get_utms'),
]