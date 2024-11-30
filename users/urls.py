from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.CustomLoginView.as_view(), name='login'),
    path("signup/", views.signup, name="signup"), 
]