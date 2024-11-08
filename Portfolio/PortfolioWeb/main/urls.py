from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('en', views.home_en, name='home_en'),
]
