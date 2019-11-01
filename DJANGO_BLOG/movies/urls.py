from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('', views.index, name='index'),
]