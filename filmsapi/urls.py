from django.urls import path
from filmsapi import views

urlpatterns = [
    path('filmsapi/', views.Movies_list),
    path('filmsapi/<int:pk>/Movieslist', views.Movies_details),
]