from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),  #Like amazon.in, homepage render directly
    path('about/', views.about, name="about"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio2/', views.portfolio2, name="portfolio2"),
    path('portfolio3/', views.portfolio3, name="portfolio3"),
    path('portfolio4/', views.portfolio4, name="portfolio4"),
    path('portfolio5/', views.portfolio5, name="portfolio5"),
    path('portfolio6/', views.portfolio6, name="portfolio6"),
    path('personal/', views.personal, name="personal"),
]