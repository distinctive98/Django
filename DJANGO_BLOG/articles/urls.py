from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    #path('new/', views.new),
    path('', views.index, name="index"),
]