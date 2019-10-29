from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('papago/', views.papago),
    path('translated/', views.translated),
    path('', views.index),
]