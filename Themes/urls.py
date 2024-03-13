from django.urls import path
from . import views

urlpatterns = [
    path('', views.themes_list, name='themes_list'),
]
