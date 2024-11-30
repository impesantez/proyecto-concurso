from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name='login'),
    path("signup/", views.signup, name="signup"), 
]