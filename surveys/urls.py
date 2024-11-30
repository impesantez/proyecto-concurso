from django.urls import path
from . import views

app_name = 'surveys'

urlpatterns = [
    path('survey/', views.survey_view, name='survey'),
]