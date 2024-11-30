from django.urls import path
from . import views

app_name = 'surveys'

urlpatterns = [
    path('', views.home, name='home'),
    path('survey/', views., name=''),
]