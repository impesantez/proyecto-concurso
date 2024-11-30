from django.urls import path
from . import views

app_name = 'electricity'

urlpatterns = [
    path('', views.index, name='index'),
    #path('calculate/', views.calculate_footprint, name='calculate_footprint'),
]