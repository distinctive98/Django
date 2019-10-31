from django.urls import path
from . import views

app_name = 'doppelganger'

urlpatterns = [
    path('confirm', views.confirm, name="confirm"),
    path('', views.main, name="main"),    
]
