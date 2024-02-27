from django.urls import path

from .views import anasayfa,about


urlpatterns = [
    path('', anasayfa, name="anasayfa"),
    path('about/', about, name="about"),
    
]